from PRICE.APIs.deposit.models.deposit import Deposits, DepositsKeys
from PRICE.base.common.response import CommonResponse


class GetDeposits(CommonResponse):
    ADD_KEYS = [DepositsKeys.DEPOSITS]
    SUB_MODELS = [Deposits]
