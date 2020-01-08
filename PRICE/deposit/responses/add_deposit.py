from PRICE.common.response import CommonResponse
from PRICE.deposit.models.add_deposit import AddDepositKeys


class AddDeposit(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [AddDepositKeys.DEPOSIT_ID, AddDepositKeys.DEPOSIT_ACCOUNT_ID]
        self._combine_args(keys=self._VARS)

        super().__init__(keys=self._VARS, **kwargs)
