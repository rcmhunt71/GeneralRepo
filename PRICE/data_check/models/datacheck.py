from dataclasses import dataclass

from PRICE.abstract.base_response import BaseResponse, BaseListResponse


@dataclass
class DataCheckKeys:
    DATA_CHECK_ID: str = "DataCheckID"
    NAME: str = "Name"
    DESCRIPTION: str = "Description"
    RESULT: str = "Result"


@dataclass
class EvaluateDataCheckBundleKeys:
    DATA_CHECKS: str = "DataChecks"


class DataCheck(BaseResponse):
    ADD_KEYS = [DataCheckKeys.DATA_CHECK_ID, DataCheckKeys.NAME,
                DataCheckKeys.DESCRIPTION, DataCheckKeys.RESULT, ]


class DataChecks(BaseListResponse):
    SUB_MODEL = DataCheck
