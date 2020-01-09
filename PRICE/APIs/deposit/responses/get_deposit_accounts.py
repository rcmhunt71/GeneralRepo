from PRICE.APIs.deposit.models.deposit_account import DepositAccounts, DepositAccountsKeys
from PRICE.base.common.response import CommonResponse


class GetDepositAccounts(CommonResponse):
    ADD_KEYS = [DepositAccountsKeys.DEPOSIT_ACCOUNTS]
    SUB_MODELS = [DepositAccounts]
