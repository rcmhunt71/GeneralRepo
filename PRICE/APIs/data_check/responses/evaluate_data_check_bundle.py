from PRICE.APIs.data_check.models.datacheck import DataChecks, EvaluateDataCheckBundleKeys
from PRICE.base.common.response import CommonResponse


class EvaluateDataCheckBundle(CommonResponse):
    ADD_KEYS = [EvaluateDataCheckBundleKeys.DATA_CHECKS]
    SUB_MODELS = [DataChecks]
