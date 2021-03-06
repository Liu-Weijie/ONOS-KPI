# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: e2sm_kpm_v2/v2/e2sm_kpm_v2.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class TestCondExpression(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn:116{TestCond-Expression}"""

    TEST_COND_EXPRESSION_EQUAL = 0
    TEST_COND_EXPRESSION_GREATERTHAN = 1
    TEST_COND_EXPRESSION_LESSTHAN = 2
    TEST_COND_EXPRESSION_CONTAINS = 3
    TEST_COND_EXPRESSION_PRESENT = 4


class Gbr(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:106{-}"""

    GBR_TRUE = 0


class Ambr(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:107{-}"""

    AMBR_TRUE = 0


class Isstat(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:108{-}"""

    ISSTAT_TRUE = 0


class Iscatm(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:109{-}"""

    ISCATM_TRUE = 0


class Rsrp(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:110{-}"""

    RSRP_TRUE = 0


class Rsrq(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:111{-}"""

    RSRQ_TRUE = 0


class IncompleteFlag(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:272{-}"""

    INCOMPLETE_FLAG_TRUE = 0


class Sum(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:82{-}"""

    SUM_TRUE = 0


class PreLabelOverride(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:86{-}"""

    PRE_LABEL_OVERRIDE_TRUE = 0


class StartEndInd(betterproto.Enum):
    """enumerated from e2sm_kpm_v2.0.2-rm.asn1:87{-}"""

    START_END_IND_START = 0
    START_END_IND_END = 1


@dataclass(eq=False, repr=False)
class Eutracgi(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:24{EUTRACGI}"""

    p_lmn_identity: "PlmnIdentity" = betterproto.message_field(1)
    e_utracell_identity: "EutracellIdentity" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Nrcgi(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:30{NRCGI}"""

    p_lmn_identity: "PlmnIdentity" = betterproto.message_field(1)
    n_rcell_identity: "NrcellIdentity" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CellGlobalId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:36{CellGlobalID}"""

    nr_cgi: "Nrcgi" = betterproto.message_field(1, group="cell_global_id")
    e_utra_cgi: "Eutracgi" = betterproto.message_field(2, group="cell_global_id")


@dataclass(eq=False, repr=False)
class Snssai(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:42{SNSSAI}"""

    s_st: bytes = betterproto.bytes_field(1)
    s_d: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class FiveQi(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:47{FiveQI}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class Qci(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:49{QCI}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class Qfi(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:51{QFI}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class Arp(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:53{ARP}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class GranularityPeriod(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:65{GranularityPeriod}"""

    value: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class MeasurementType(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:66{MeasurementType}"""

    meas_name: "MeasurementTypeName" = betterproto.message_field(
        1, group="measurement_type"
    )
    meas_id: "MeasurementTypeId" = betterproto.message_field(
        2, group="measurement_type"
    )


@dataclass(eq=False, repr=False)
class MeasurementTypeId(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:73{MeasurementTypeID}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MeasurementLabel(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:76{MeasurementLabel}"""

    plmn_id: "PlmnIdentity" = betterproto.message_field(1)
    slice_id: "Snssai" = betterproto.message_field(2)
    five_qi: "FiveQi" = betterproto.message_field(3)
    q_fi: "Qfi" = betterproto.message_field(4)
    q_ci: "Qci" = betterproto.message_field(5)
    q_cimax: "Qci" = betterproto.message_field(6)
    q_cimin: "Qci" = betterproto.message_field(7)
    a_rpmax: "Arp" = betterproto.message_field(8)
    a_rpmin: "Arp" = betterproto.message_field(9)
    bitrate_range: int = betterproto.int32_field(10)
    layer_mu_mimo: int = betterproto.int32_field(11)
    s_um: "Sum" = betterproto.enum_field(12)
    dist_bin_x: int = betterproto.int32_field(13)
    dist_bin_y: int = betterproto.int32_field(14)
    dist_bin_z: int = betterproto.int32_field(15)
    pre_label_override: "PreLabelOverride" = betterproto.enum_field(16)
    start_end_ind: "StartEndInd" = betterproto.enum_field(17)


@dataclass(eq=False, repr=False)
class SubscriptionId(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:96{SubscriptionID}"""

    value: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class TestCondInfo(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:99{TestCondInfo}"""

    test_type: "TestCondType" = betterproto.message_field(1)
    test_expr: "TestCondExpression" = betterproto.enum_field(2)
    test_value: "TestCondValue" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class TestCondType(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:106{TestCond-Type}"""

    g_br: "Gbr" = betterproto.enum_field(1, group="test_cond_type")
    a_mbr: "Ambr" = betterproto.enum_field(2, group="test_cond_type")
    is_stat: "Isstat" = betterproto.enum_field(3, group="test_cond_type")
    is_cat_m: "Iscatm" = betterproto.enum_field(4, group="test_cond_type")
    r_srp: "Rsrp" = betterproto.enum_field(5, group="test_cond_type")
    r_srq: "Rsrq" = betterproto.enum_field(6, group="test_cond_type")


@dataclass(eq=False, repr=False)
class TestCondValue(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:125{TestCond-Value}"""

    value_int: int = betterproto.int64_field(1, group="test_cond_value")
    value_enum: int = betterproto.int64_field(2, group="test_cond_value")
    value_bool: bool = betterproto.bool_field(3, group="test_cond_value")
    value_bit_s: "BitString" = betterproto.message_field(4, group="test_cond_value")
    value_oct_s: str = betterproto.string_field(5, group="test_cond_value")
    value_prt_s: str = betterproto.string_field(6, group="test_cond_value")


@dataclass(eq=False, repr=False)
class GlobalKpmnodeId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:137{GlobalKPMv2node-ID}"""

    g_nb: "GlobalKpmnodeGnbId" = betterproto.message_field(1, group="global_kpmnode_id")
    en_g_nb: "GlobalKpmnodeEnGnbId" = betterproto.message_field(
        2, group="global_kpmnode_id"
    )
    ng_e_nb: "GlobalKpmnodeNgEnbId" = betterproto.message_field(
        3, group="global_kpmnode_id"
    )
    e_nb: "GlobalKpmnodeEnbId" = betterproto.message_field(4, group="global_kpmnode_id")


@dataclass(eq=False, repr=False)
class GlobalKpmnodeGnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:145{GlobalKPMv2node-gNB-ID}"""

    global_g_nb_id: "GlobalgNbId" = betterproto.message_field(1)
    g_nb_cu_up_id: "GnbCuUpId" = betterproto.message_field(2)
    g_nb_du_id: "GnbDuId" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class GlobalgNbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:152{GlobalgNB-ID}"""

    plmn_id: "PlmnIdentity" = betterproto.message_field(1)
    gnb_id: "GnbIdChoice" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GnbCuUpId(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:157{GNB-CU-UP-ID}"""

    value: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class GnbDuId(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:159{GNB-DU-ID}"""

    value: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class GnbIdChoice(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:162{GNB-ID-Choice}"""

    gnb_id: "BitString" = betterproto.message_field(1, group="gnb_id_choice")


@dataclass(eq=False, repr=False)
class GlobalKpmnodeEnGnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:167{GlobalKPMv2node-en-gNB-ID}"""

    global_g_nb_id: "GlobalenGnbId" = betterproto.message_field(1)
    g_nb_cu_up_id: "GnbCuUpId" = betterproto.message_field(2)
    g_nb_du_id: "GnbDuId" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class GlobalenGnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:174{GlobalenGNB-ID}"""

    p_lmn_identity: "PlmnIdentity" = betterproto.message_field(1)
    g_nb_id: "EngnbId" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class EngnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:180{ENGNB-ID}"""

    g_nb_id: "BitString" = betterproto.message_field(1, group="engnb_id")


@dataclass(eq=False, repr=False)
class GlobalKpmnodeNgEnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:185{GlobalKPMv2node-ng-eNB-ID}"""

    global_ng_e_nb_id: "GlobalngeNbId" = betterproto.message_field(1)
    g_nb_du_id: "GnbDuId" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GlobalngeNbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:191{GlobalngeNB-ID-KPMv2}"""

    plmn_id: "PlmnIdentity" = betterproto.message_field(1)
    enb_id: "EnbIdChoice" = betterproto.message_field(2)
    short_macro_e_nb_id: "BitString" = betterproto.message_field(3)
    long_macro_e_nb_id: "BitString" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class EnbIdChoice(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:199{ENB-ID-Choice}"""

    enb_id_macro: "BitString" = betterproto.message_field(1, group="enb_id_choice")
    enb_id_shortmacro: "BitString" = betterproto.message_field(2, group="enb_id_choice")
    enb_id_longmacro: "BitString" = betterproto.message_field(3, group="enb_id_choice")


@dataclass(eq=False, repr=False)
class GlobalKpmnodeEnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:206{GlobalKPMv2node-eNB-ID}"""

    global_e_nb_id: "GlobalEnbId" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GlobalEnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:211{GlobalENB-ID}"""

    p_lmn_identity: "PlmnIdentity" = betterproto.message_field(1)
    e_nb_id: "EnbId" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class EnbId(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:217{ENB-ID-KPMv2}"""

    macro_e_nb_id: "BitString" = betterproto.message_field(1, group="enb_id")
    home_e_nb_id: "BitString" = betterproto.message_field(2, group="enb_id")


@dataclass(eq=False, repr=False)
class RanfunctionName(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:225{RANfunction-Name}"""

    ran_function_short_name: str = betterproto.string_field(1)
    ran_function_e2_sm_oid: str = betterproto.string_field(2)
    ran_function_description: str = betterproto.string_field(3)
    ran_function_instance: int = betterproto.int32_field(4)


@dataclass(eq=False, repr=False)
class RicStyleType(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:234{RIC-Style-Type}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class RicFormatType(betterproto.Message):
    """range of Integer from e2sm_kpm_v2.0.2-rm.asn:242{RIC-Format-Type}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofKpmnodes(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:242{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofCells(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:243{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofRicstyles(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:244{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofMeasurementInfo(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:245{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofLabelInfo(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:246{-}"""

    value: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofMeasurementRecord(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:247{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofMeasurementValue(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:248{-}"""

    value: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofConditionInfo(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:249{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MaxnoofUeid(betterproto.Message):
    """constant Integer from e2sm_kpm_v2.0.2-rm.asn:250{-}"""

    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MeasurementInfoList(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:255{MeasurementInfoList}"""

    value: List["MeasurementInfoItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementInfoItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:256{MeasurementInfoItem}"""

    meas_type: "MeasurementType" = betterproto.message_field(1)
    label_info_list: "LabelInfoList" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class LabelInfoList(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:263{LabelInfoList}"""

    value: List["LabelInfoItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class LabelInfoItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:264{LabelInfoItem}"""

    meas_label: "MeasurementLabel" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementData(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:270{MeasurementData}"""

    value: List["MeasurementDataItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementDataItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:271{MeasurementDataItem}"""

    meas_record: "MeasurementRecord" = betterproto.message_field(1)
    incomplete_flag: "IncompleteFlag" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class MeasurementRecord(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:278{MeasurementRecord}"""

    value: List["MeasurementRecordItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementRecordItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:279{MeasurementRecordItem}"""

    integer: int = betterproto.int64_field(1, group="measurement_record_item")
    real: float = betterproto.double_field(2, group="measurement_record_item")
    no_value: int = betterproto.int32_field(3, group="measurement_record_item")


@dataclass(eq=False, repr=False)
class MeasurementInfoActionList(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:287{MeasurementInfo-Action-List}
    """

    value: List["MeasurementInfoActionItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementInfoActionItem(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:288{MeasurementInfo-Action-Item}
    """

    meas_name: "MeasurementTypeName" = betterproto.message_field(1)
    meas_id: "MeasurementTypeId" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MeasurementCondList(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:295{MeasurementCondList}"""

    value: List["MeasurementCondItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementCondItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:296{MeasurementCondItem}"""

    meas_type: "MeasurementType" = betterproto.message_field(1)
    matching_cond: "MatchingCondList" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MeasurementCondUeidList(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:303{MeasurementCondUEidList}"""

    value: List["MeasurementCondUeidItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementCondUeidItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:304{MeasurementCondUEidItem}"""

    meas_type: "MeasurementType" = betterproto.message_field(1)
    matching_cond: "MatchingCondList" = betterproto.message_field(2)
    matching_ueid_list: "MatchingUeidList" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class MatchingCondList(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:312{MatchingCondList}"""

    value: List["MatchingCondItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MatchingCondItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:313{MatchingCondItem}"""

    meas_label: "MeasurementLabel" = betterproto.message_field(
        1, group="matching_cond_item"
    )
    test_cond_info: "TestCondInfo" = betterproto.message_field(
        2, group="matching_cond_item"
    )


@dataclass(eq=False, repr=False)
class MatchingUeidList(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:320{MatchingUEidList}"""

    value: List["MatchingUeidItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MatchingUeidItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:321{MatchingUEidItem}"""

    ue_id: "UeIdentity" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class E2SmKpmEventTriggerDefinition(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:337{E2SM-KPMv2-EventTriggerDefinition}
    """

    event_definition_format1: "E2SmKpmEventTriggerDefinitionFormat1" = (
        betterproto.message_field(1, group="e2_sm_kpm_event_trigger_definition")
    )


@dataclass(eq=False, repr=False)
class E2SmKpmEventTriggerDefinitionFormat1(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:342{E2SM-KPMv2-EventTriggerDefinition-
    Format1}
    """

    reporting_period: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class E2SmKpmActionDefinition(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:351{E2SM-KPMv2-ActionDefinition}
    """

    ric_style_type: "RicStyleType" = betterproto.message_field(1)
    action_definition_format1: "E2SmKpmActionDefinitionFormat1" = (
        betterproto.message_field(2, group="e2_sm_kpm_action_definition")
    )
    action_definition_format2: "E2SmKpmActionDefinitionFormat2" = (
        betterproto.message_field(3, group="e2_sm_kpm_action_definition")
    )
    action_definition_format3: "E2SmKpmActionDefinitionFormat3" = (
        betterproto.message_field(4, group="e2_sm_kpm_action_definition")
    )


@dataclass(eq=False, repr=False)
class E2SmKpmActionDefinitionFormat1(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:362{E2SM-KPMv2-ActionDefinition-
    Format1}
    """

    cell_obj_id: "CellObjectId" = betterproto.message_field(1)
    meas_info_list: "MeasurementInfoList" = betterproto.message_field(2)
    granul_period: "GranularityPeriod" = betterproto.message_field(3)
    subscript_id: "SubscriptionId" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class E2SmKpmActionDefinitionFormat2(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:370{E2SM-KPMv2-ActionDefinition-
    Format2}
    """

    ue_id: "UeIdentity" = betterproto.message_field(1)
    subscript_info: "E2SmKpmActionDefinitionFormat1" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class E2SmKpmActionDefinitionFormat3(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:376{E2SM-KPMv2-ActionDefinition-
    Format3}
    """

    cell_obj_id: "CellObjectId" = betterproto.message_field(1)
    meas_cond_list: "MeasurementCondList" = betterproto.message_field(2)
    granul_period: "GranularityPeriod" = betterproto.message_field(3)
    subscript_id: "SubscriptionId" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class E2SmKpmIndicationHeader(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:391{E2SM-KPMv2-IndicationHeader}
    """

    indication_header_format1: "E2SmKpmIndicationHeaderFormat1" = (
        betterproto.message_field(1, group="e2_sm_kpm_indication_header")
    )


@dataclass(eq=False, repr=False)
class E2SmKpmIndicationHeaderFormat1(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:396{E2SM-KPMv2-IndicationHeader-
    Format1}
    """

    collet_start_time: "TimeStamp" = betterproto.message_field(1)
    file_formatversion: str = betterproto.string_field(2)
    sender_name: str = betterproto.string_field(3)
    sender_type: str = betterproto.string_field(4)
    vendor_name: str = betterproto.string_field(5)
    kpm_node_id: "GlobalKpmnodeId" = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class E2SmKpmIndicationMessage(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:414{E2SM-KPMv2-IndicationMessage}
    """

    indication_message_format1: "E2SmKpmIndicationMessageFormat1" = (
        betterproto.message_field(1, group="e2_sm_kpm_indication_message")
    )
    indication_message_format2: "E2SmKpmIndicationMessageFormat2" = (
        betterproto.message_field(2, group="e2_sm_kpm_indication_message")
    )


@dataclass(eq=False, repr=False)
class E2SmKpmIndicationMessageFormat1(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:419{E2SM-KPMv2-IndicationMessage-
    Format1}
    """

    subscript_id: "SubscriptionId" = betterproto.message_field(1)
    cell_obj_id: "CellObjectId" = betterproto.message_field(2)
    granul_period: "GranularityPeriod" = betterproto.message_field(3)
    meas_info_list: "MeasurementInfoList" = betterproto.message_field(4)
    meas_data: "MeasurementData" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class E2SmKpmIndicationMessageFormat2(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:428{E2SM-KPMv2-IndicationMessage-
    Format2}
    """

    subscript_id: "SubscriptionId" = betterproto.message_field(1)
    cell_obj_id: "CellObjectId" = betterproto.message_field(2)
    granul_period: "GranularityPeriod" = betterproto.message_field(3)
    meas_cond_ueid_list: "MeasurementCondUeidList" = betterproto.message_field(4)
    meas_data: "MeasurementData" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class E2SmKpmRanfunctionDescription(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:441{E2SM-KPMv2-RANfunction-
    Description}
    """

    ran_function_name: "RanfunctionName" = betterproto.message_field(1)
    ric_kpm_node_list: List["RicKpmnodeItem"] = betterproto.message_field(2)
    ric_event_trigger_style_list: List[
        "RicEventTriggerStyleItem"
    ] = betterproto.message_field(3)
    ric_report_style_list: List["RicReportStyleItem"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class RicKpmnodeItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:449{RIC-KPMNode-Item}"""

    ric_kpmnode_type: "GlobalKpmnodeId" = betterproto.message_field(1)
    cell_measurement_object_list: List[
        "CellMeasurementObjectItem"
    ] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CellMeasurementObjectItem(betterproto.Message):
    """
    sequence from e2sm_kpm_v2.0.2-rm.asn:455{Cell-Measurement-Object-Item}
    """

    cell_object_id: "CellObjectId" = betterproto.message_field(1)
    cell_global_id: "CellGlobalId" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class RicEventTriggerStyleItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:461{RIC-EventTriggerStyle-Item}"""

    ric_event_trigger_style_type: "RicStyleType" = betterproto.message_field(1)
    ric_event_trigger_style_name: "RicStyleName" = betterproto.message_field(2)
    ric_event_trigger_format_type: "RicFormatType" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class RicReportStyleItem(betterproto.Message):
    """sequence from e2sm_kpm_v2.0.2-rm.asn:468{RIC-ReportStyle-Item}"""

    ric_report_style_type: "RicStyleType" = betterproto.message_field(1)
    ric_report_style_name: "RicStyleName" = betterproto.message_field(2)
    ric_action_format_type: "RicFormatType" = betterproto.message_field(3)
    meas_info_action_list: "MeasurementInfoActionList" = betterproto.message_field(4)
    ric_indication_header_format_type: "RicFormatType" = betterproto.message_field(5)
    ric_indication_message_format_type: "RicFormatType" = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class RicStyleName(betterproto.Message):
    """{RIC-Style-Name}"""

    value: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CellObjectId(betterproto.Message):
    """{CellObjectID}"""

    value: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MeasurementTypeName(betterproto.Message):
    """{MeasurementTypeName}"""

    value: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class UeIdentity(betterproto.Message):
    """{UE-Identity}"""

    value: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PlmnIdentity(betterproto.Message):
    """{PLMN-Identity}"""

    value: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class TimeStamp(betterproto.Message):
    """{TimeStamp}"""

    value: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class EutracellIdentity(betterproto.Message):
    """{EUTRACellIdentity}"""

    value: "BitString" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class NrcellIdentity(betterproto.Message):
    """{NRCellIdentity}"""

    value: "BitString" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class BitString(betterproto.Message):
    """{BIT_STRING}"""

    value: bytes = betterproto.bytes_field(1)
    len: int = betterproto.uint32_field(2)
