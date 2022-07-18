import cgi
from cgitb import handler
import os
import asyncio
import logging
from typing import AnyStr, Dict, List
from argparse import ArgumentParser, Namespace

import onos_ric_sdk_py as ricsdk
from onos_ric_sdk_py import E2Client, SDLClient
from onos_api.e2t.e2.v1beta1 import (
    Action,
    ActionType,
    SubsequentAction,
    SubsequentActionType,
    TimeToWait
)
from onos_e2_sm.asn1.v1 import BitString

from onos_e2_sm.e2sm_rc_pre.v2 import (
    E2SmRcPreControlHeader,
    E2SmRcPreControlHeaderFormat1,
    E2SmRcPreControlMessage,
    E2SmRcPreControlMessageFormat1,
    E2SmRcPreEventTriggerDefinition,
    E2SmRcPreEventTriggerDefinitionFormat1,
    E2SmRcPreIndicationHeader,
    E2SmRcPreIndicationMessage,
    RcPreTriggerType,
    Nrt,
    RcPreCommand,
    RicControlMessagePriority,
    RanparameterDefItem,
    RanparameterId,
    RanparameterItem,
    RanparameterName,
    RanparameterType,
    RanparameterValue,
)

from onos_e2_sm.e2sm_rc.v1 import (
    AmfUeNgapId,
    Amfpointer,
    AmfregionId,
    AmfsetId,
    E2SmRcControlHeader,
    E2SmRcControlHeaderFormat1,
    E2SmRcControlMessage,
    E2SmRcControlMessageFormat1,
    E2SmRcControlMessageFormat1Item,
    E2SmRcEventTrigger,
    E2SmRcEventTriggerFormat1Item,
    E2SmRcEventTriggerFormat1,
    E2SmRcEventTriggerFormat3Item,
    E2SmRcEventTriggerFormat3,
    GlobalGnbId,
    GlobalNgEnbId,
    GlobalNgrannodeId,
    GnbCuCpUeE1ApId,
    GnbCuUeF1ApId,
    GnbId,
    Guami,
    NgEnbId,
    NgRannodeUexnApid,
    Plmnidentity,
    RanparameterStructure,
    RanparameterStructureItem,
    RanparameterValueType,
    RanparameterValueTypeChoiceElementFalse,
    RanparameterValueTypeChoiceStructure,
    Ranueid,
    RicActionDefinitionFormats,
    RicControlActionId,
    RicControlHeaderFormats,
    RicControlMessageFormats,
    RicEventTriggerConditionId,
    E2SmRcActionDefinition,
    E2SmRcActionDefinitionFormat1,
    E2SmRcActionDefinitionFormat1Item,
    E2SmRcIndicationHeader,
    E2SmRcIndicationHeaderFormat1,
    E2SmRcIndicationMessage,
    E2SmRcActionDefinitionFormat1,
    E2SmRcActionDefinitionFormat1Item,
    RanparameterId,
    RicEventTriggerFormats,
    RicStyleType,
    Ueid,
    UeidGnb,
    UeidGnbCuCpE1ApIdItem,
    UeidGnbCuCpE1ApIdList,
    UeidGnbCuCpF1ApIdItem,
    UeidGnbCuF1ApIdList,
)

# service model name and version
ServiceModelName = 'oran-e2sm-rc'
ServiceModelVersion = 'v1'
# pci trigger type
# RcPreTriggerTypes = [RcPreTriggerType.RC_PRE_TRIGGER_TYPE_PERIODIC, RcPreTriggerType.RC_PRE_TRIGGER_TYPE_UPON_CHANGE]

async def run(e2_client: E2Client, e2_node_id: str, kpi: Dict[str,int], lock: asyncio.Lock):
    subscriptions = [
        subscribe(e2_client, e2_node_id, kpi, lock)
    ]
    await asyncio.gather(*subscriptions)

def create_event_trigger(trigger_type: RcPreTriggerType, period=1000) -> E2SmRcPreEventTriggerDefinition:
    trigger = E2SmRcPreEventTriggerDefinition()
    format1 = E2SmRcPreEventTriggerDefinitionFormat1(
        trigger_type=trigger_type,
        reporting_period_ms=period,
    )
    trigger.event_definition_format1 = format1
    return trigger

def create_event_trigger_definition():
    e2_node_info_changed = E2SmRcEventTriggerFormat3Item(
        ric_event_trigger_condition_id=RicEventTriggerConditionId(value=1),
        e2_node_info_change_id=2,
    )

    item_list : List = [e2_node_info_changed]

    rc_event_trigger_definition = E2SmRcEventTrigger(
        ric_event_trigger_formats=RicEventTriggerFormats(
            event_trigger_format3=E2SmRcEventTriggerFormat3(
                e2_node_info_change_list=item_list,
            ),
        ),
    )

    return rc_event_trigger_definition

def create_subscription_actions():
    item_list : List = []

    item = E2SmRcActionDefinitionFormat1Item(
        ran_parameter_id=RanparameterId(value=21528),
    )

    item_list.append(item)

    rc_action_definition = E2SmRcActionDefinition(
        ric_style_type=RicStyleType(value=3),
        ric_action_definition_formats=RicActionDefinitionFormats(
            action_definition_format1=E2SmRcActionDefinitionFormat1(
                ran_p_to_be_reported_list=item_list,
            )
        )
    )

    action_report = Action(
        id=3,
        type=ActionType.ACTION_TYPE_REPORT,
        payload=bytes(rc_action_definition),
    )

    return action_report

def bytes_to_string(bs: AnyStr) -> AnyStr:
    return ''.join([f'{ch}' for ch in bs])

def handle_periodic_report(header: E2SmRcPreIndicationHeader, message: E2SmRcPreIndicationMessage) -> Dict:
    serving_nci: bytes = header.indication_header_format1.cgi.nr_cgi.n_rcell_identity.value.value
    meas_reports: List[Nrt] = message.indication_message_format1.neighbors

    return dict(
        ue_id=message.indication_message_format1.dl_arfcn.e_arfcn.value,
        serving_nci=bytes_to_string(serving_nci),
        neighbors={
            bytes_to_string(meas_report.cgi.nr_cgi.n_rcell_identity.value.value): meas_report.pci.value
            for meas_report in meas_reports
        }
    )


async def subscribe(e2_client: E2Client, e2_node_id: str, kpi: Dict[str,int], lock: asyncio.Lock):
    logging.info(f'subscription node id : {e2_node_id}')
    # create action report
    # ActionReport = Action(
    #     id=0,
    #     type=ActionType.ACTION_TYPE_REPORT,
    #     subsequent_action=SubsequentAction(
    #         type=SubsequentActionType.SUBSEQUENT_ACTION_TYPE_CONTINUE,
    #         time_to_wait=TimeToWait.TIME_TO_WAIT_ZERO
    #     )
    # )
    ActionReport = create_subscription_actions()
    logging.info(f"Action Report : {ActionReport}")
    # send subscription report
    logging.info(f'sending pci subscription for {e2_node_id}')
    async for header_bytes, message_bytes in e2_client.subscribe(
        e2_node_id=e2_node_id,
        service_model_name=ServiceModelName,
        service_model_version=ServiceModelVersion,
        subscription_id=f'onos-pci-subscription-{e2_node_id}',
        trigger=bytes(create_event_trigger_definition()),
        actions=[ActionReport]
    ):
        logging.info(f'received pci indication for {e2_node_id}')
        # get indication message
        header = E2SmRcPreIndicationHeader()
        message = E2SmRcPreIndicationMessage()
        header.parse(header_bytes)
        message.parse(message_bytes)

        # logging.info(f"indication header : {header}")
        # logging.info(f"indication message : {message}")

        # header = E2SmRcIndicationHeader()
        # message = E2SmRcIndicationMessage()
        # header.parse(header_bytes)
        # message.parse(message_bytes)

        # header_format1 = header.ric_indication_header_formats.indication_header_format1
        # message_format3 = message.ric_indication_message_formats.indication_message_format3

        # logging.info(f"indication header : {header}")
        # logging.info(f"indication header format : {header_format1}")
        # logging.info(f"indication message : {message}")
        # logging.info(f"indication message format : {message_format3}")

        # pci_data: Dict = dict()
        # pci_data = handle_periodic_report(header, message)

        # pci_data['e2_node_id'] = e2_node_id
        # pci_data['trigger_type'] = trigger_type.name

        # logging.info(f'pci_data : {pci_data}')
        async with lock:
            logging.info(f'kpi_data : {kpi}')
        # send control request
        # control header
        ControlHeader = E2SmRcPreControlHeader(
            control_header_format1=E2SmRcPreControlHeaderFormat1(
                cgi=header.indication_header_format1.cgi,
                rc_command=RcPreCommand.RC_PRE_COMMAND_SET_PARAMETERS,
                ric_control_message_priority=RicControlMessagePriority(value=5)
            )
        )

        # ControlHeader = E2SmRcControlHeader(
        #     ric_control_header_formats=RicControlHeaderFormats(
        #         control_header_format1=E2SmRcControlHeaderFormat1(
        #             ue_id=Ueid(
        #                 g_nb_ueid=UeidGnb(
        #                     amf_ue_ngap_id=AmfUeNgapId(value=0),
        #                     guami=Guami(
        #                         p_lmnidentity=Plmnidentity(value=bytes([0,0,0])),
        #                         a_mfregion_id=AmfregionId(value=BitString(
        #                             value=bytes([0]),
        #                             len=8
        #                         )),
        #                         a_mfset_id=AmfsetId(value=BitString(
        #                             value=bytes([0,0]),
        #                             len=10,
        #                         )),
        #                         a_mfpointer=Amfpointer(value=BitString(
        #                             value=bytes([0]),
        #                             len=6,    
        #                         ))
        #                     ),
        #                     g_nb_cu_ue_f1_ap_id_list=UeidGnbCuF1ApIdList(
        #                         value=[UeidGnbCuCpF1ApIdItem(
        #                             g_nb_cu_ue_f1_ap_id=GnbCuUeF1ApId(
        #                                 value=0,
        #                             ),
        #                         )],
        #                     ),
        #                     g_nb_cu_cp_ue_e1_ap_id_list=UeidGnbCuCpE1ApIdList(
        #                         value=[UeidGnbCuCpE1ApIdItem(
        #                             g_nb_cu_cp_ue_e1_ap_id=GnbCuCpUeE1ApId(
        #                                 value=0,
        #                             ),
        #                         )],
        #                     ),
        #                     ran_ueid=Ranueid(value=bytes([0,0,0,0,0,0,0,0])),
        #                     m_ng_ran_ue_xn_ap_id=NgRannodeUexnApid(value=0),
        #                     global_gnb_id=GlobalGnbId(
        #                         p_lmnidentity=Plmnidentity(
        #                             value=bytes([0,0,0]),
        #                         ),
        #                         g_nb_id=GnbId(
        #                             g_nb_id=BitString(
        #                                 value=bytes([0,0,0,0]),
        #                                 len=32,
        #                             )
        #                         ),
        #                     ),
        #                     global_ng_rannode_id=GlobalNgrannodeId(
        #                         g_nb=GlobalGnbId(
        #                             p_lmnidentity=Plmnidentity(
        #                                 value=bytes([0,0,0]),
        #                             ),
        #                             g_nb_id=GnbId(
        #                                 g_nb_id=BitString(
        #                                     value=bytes([0,0,0,0]),
        #                                     len=32,
        #                                 )
        #                             ),
        #                         ),
        #                         ng_e_nb=GlobalNgEnbId(
        #                             p_lmnidentity=Plmnidentity(
        #                                 value=bytes([0,0,0]),
        #                             ),
        #                             ng_enb_id=NgEnbId(
        #                                 macro_ng_enb_id=BitString(
        #                                     value=bytes([0,0,0,0]),
        #                                     len=32,
        #                                 )
        #                             ),
        #                         ),
        #                     ),
        #                 ),
        #             ),
        #             ric_style_type=RicStyleType(value=9),
        #             ric_control_action_id=RicControlActionId(value=1),
        #         ),
        #     ),
        # )

        logging.info(f"control head : {ControlHeader}")
        # control message
        ControlMessage = E2SmRcPreControlMessage(
            control_message=E2SmRcPreControlMessageFormat1(
                parameter_type=RanparameterDefItem(
                    ran_parameter_id=RanparameterId(value=1),
                    ran_parameter_name=RanparameterName(value="Result"),
                    ran_parameter_type=RanparameterType.RANPARAMETER_TYPE_INTEGER,
                ),
                parameter_val=RanparameterValue(
                    value_int=1
                ),
            )
        )

        # ranparamter_list : List = []

        # sequence_of_ran_parameters_1 : List = []

        # ran_paramter_structure_item = RanparameterStructureItem(
        #     ran_parameter_id=RanparameterId(value=1),
        #     ran_parameter_value_type=RanparameterValueType(
        #         ran_p_choice_element_false=RanparameterValueTypeChoiceElementFalse(
        #             ran_parameter_value=RanparameterValue(
        #                 value_int=100
        #             ),
        #         ),
        #     ),
        # ) 


        # sequence_of_ran_parameters_1.append(ran_paramter_structure_item)

        # ranparamter1 = E2SmRcControlMessageFormat1Item(
        #     ran_parameter_id=RanparameterId(value=1),
        #     ran_parameter_value_type=RanparameterValueType(
        #         ran_p_choice_structure=RanparameterValueTypeChoiceStructure(
        #             ran_parameter_structure=RanparameterStructure(
        #                 sequence_of_ran_parameters=sequence_of_ran_parameters_1,
        #             )
        #         )
        #     )
        # )

        # ranparamter_list.append(ranparamter1)

        # ControlMessage = E2SmRcControlMessage(
        #     ric_control_message_formats=RicControlMessageFormats(
        #         control_message_format1=E2SmRcControlMessageFormat1(
        #             ran_p_list=ranparamter_list,
        #         ),
        #     ),
        # )
        logging.info(f"control message : {ControlMessage}")

        logging.info(f'sending control request for {e2_node_id}')
        
        try:
            await e2_client.control(
                e2_node_id=e2_node_id,
                service_model_name=ServiceModelName,
                service_model_version=ServiceModelVersion,
                header=bytes(ControlHeader),
                message=bytes(ControlMessage)
            )
        except Exception as e:
            logging.error(f'control failure: {e.args}')
        else:      
            logging.info(f"control success")
