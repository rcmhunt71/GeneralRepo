from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DepositAccountKeys:
    CUSTOMER_ID: str = "CustomerID"
    DEPOSIT_ID: str = "DepositID"
    DEPOSIT_ACCOUNT_ID: str = "DepositAccountID"
    ACCOUNT_TYPE: str = "AccountType"
    ACCOUNT_NUMBER: str = "AccountNumber"
    ACCOUNT_NAME: str = "AccountName"
    BALANCE: str = "Balance"
    FIELDS: str = "Fields"


@dataclass
class DepositAccountsKeys:
    DEPOSIT_ACCOUNTS: str = "DepositAccounts"


@dataclass
class DepositAccountsFieldsKeys:
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


class DepositAccount(BaseResponse):
    ADD_KEYS = [
        DepositAccountKeys.CUSTOMER_ID, DepositAccountKeys.DEPOSIT_ID, DepositAccountKeys.DEPOSIT_ACCOUNT_ID,
        DepositAccountKeys.ACCOUNT_TYPE, DepositAccountKeys.ACCOUNT_NUMBER, DepositAccountKeys.ACCOUNT_NAME,
        DepositAccountKeys.BALANCE]
    SUB_MODELS = None


class DepositAccounts(BaseListResponse):
    SUB_MODEL = DepositAccount


class DepositAccountFieldEntry(BaseResponse):
    ADD_KEYS = [DepositAccountsFieldsKeys.FIELD_NAME, DepositAccountsFieldsKeys.FIELD_VALUE]
    SUB_MODELS = None


class DepositAccountFieldList(BaseListResponse):
    SUB_MODEL = DepositAccountFieldEntry


class DepositAccountRequestModel(BaseResponse):
    ADD_KEYS = [DepositAccountKeys.CUSTOMER_ID, DepositAccountKeys.DEPOSIT_ID,
                DepositAccountKeys.DEPOSIT_ACCOUNT_ID, DepositAccountKeys.FIELDS]
    SUB_MODELS = [None, None, None, DepositAccountFieldList]
