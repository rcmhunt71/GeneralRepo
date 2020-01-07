from PRICE.common.response import CommonResponse
from PRICE.deposit.models.deposit import Deposits, DepositsKeys


class GetDeposits(CommonResponse):
    def __init__(self, keys=None, objs=None, **kwargs):

        deposit_key = DepositsKeys.DEPOSITS
        self._OBJS = [deposit_key]
        kwargs[deposit_key] = Deposits(*kwargs.get(deposit_key))
        super().__init__(keys=keys, objs=self._OBJS, **kwargs)