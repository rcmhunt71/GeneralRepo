from PRICE.common.response import CommonResponse
from PRICE.deposit.models.deposit_account import DepositAccounts, DepositAccountsKeys


class GetDepositAccounts(CommonResponse):
    def __init__(self, keys=None, objs=None, **kwargs):

        deposit_key = DepositAccountsKeys.DEPOSIT_ACCOUNTS
        self._OBJS = [deposit_key]
        kwargs[deposit_key] = DepositAccounts(*kwargs.get(deposit_key))
        super().__init__(keys=keys, objs=self._OBJS, **kwargs)
