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

# service model name and version
ServiceModelName = 'oran-e2sm-rc-pre'
ServiceModelVersion = 'v2'
# pci trigger type
RcPreTriggerTypes = [RcPreTriggerType.RC_PRE_TRIGGER_TYPE_PERIODIC, RcPreTriggerType.RC_PRE_TRIGGER_TYPE_UPON_CHANGE]

async def run(e2_client: E2Client, e2_node_id: str, kpi: Dict[str,int], lock: asyncio.Lock):
    subscriptions = [
        subscribe(e2_client, e2_node_id, RcPreTriggerType, kpi, lock)
        for RcPreTriggerType in RcPreTriggerTypes
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


async def subscribe(e2_client: E2Client, e2_node_id: str, trigger_type: RcPreTriggerType, kpi: Dict[str,int], lock: asyncio.Lock):
    logging.info(f'subscription node id : {e2_node_id} type : {trigger_type}')
    # create action report
    ActionReport = Action(
        id=0,
        type=ActionType.ACTION_TYPE_REPORT,
        subsequent_action=SubsequentAction(
            type=SubsequentActionType.SUBSEQUENT_ACTION_TYPE_CONTINUE,
            time_to_wait=TimeToWait.TIME_TO_WAIT_ZERO
        )
    )
    logging.info(f"Action Report : {ActionReport}")
    # send subscription report
    logging.info(f'sending pci subscription for {e2_node_id}')
    async for header_bytes, message_bytes in e2_client.subscribe(
        e2_node_id=e2_node_id,
        service_model_name=ServiceModelName,
        service_model_version=ServiceModelVersion,
        subscription_id=f'onos-pci-subscription-{e2_node_id}-{trigger_type}',
        trigger=bytes(create_event_trigger(trigger_type)),
        actions=[ActionReport]
    ):
        logging.info(f'received pci indication for {e2_node_id}')
        # get indication message
        header = E2SmRcPreIndicationHeader()
        message = E2SmRcPreIndicationMessage()
        header.parse(header_bytes)
        message.parse(message_bytes)

        logging.info(f"indication header : {header}")
        logging.info(f"indication message : {message}")

        pci_data: Dict = dict()
        pci_data = handle_periodic_report(header, message)

        pci_data['e2_node_id'] = e2_node_id
        pci_data['trigger_type'] = trigger_type.name

        logging.info(f'pci_data : {pci_data}')
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
        logging.info(f"control head : {ControlHeader}")
        # control message
        ControlMessage = E2SmRcPreControlMessage(
            control_message=E2SmRcPreControlMessageFormat1(
                parameter_type=RanparameterDefItem(
                    ran_parameter_id=RanparameterId(value=1),
                    ran_parameter_name=RanparameterName(value="result"),
                    ran_parameter_type=RanparameterType.RANPARAMETER_TYPE_INTEGER,
                ),
                parameter_val=RanparameterValue(
                    value_int=1
                )
            )
        )
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
