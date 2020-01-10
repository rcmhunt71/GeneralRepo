from PRICE.base.common.response import CommonResponse

from PRICE.APIs.liability.models.liability import LiabilityEntriesList, LiabilitiesKeys


class GetLiabilities(CommonResponse):
    ADD_KEYS = [LiabilitiesKeys.LIABILITIES]
    SUB_MODELS = [LiabilityEntriesList]
