from dataclasses import dataclass

from PRICE.abstract.base_response import BaseResponse, BaseListResponse


@dataclass
class DepositKeys:
    CUSTOMER_ID: str = "CustomerID"
    DEPOSIT_ID: str = "DepositID"
    INSTITUTION_ID: str = "InstitutionID"
    VERIFY: str = "Verify"
    VERIFY_DATA: str = "VerifyDate"
    BOTH: str = "Both"


@dataclass
class DepositsKeys:
    DEPOSITS: str = "Deposits"


class Deposit(BaseResponse):
    ADD_KEYS = [DepositKeys.CUSTOMER_ID, DepositKeys.DEPOSIT_ID, DepositKeys.INSTITUTION_ID, DepositKeys.VERIFY,
                DepositKeys.VERIFY_DATA, DepositKeys.BOTH]


class Deposits(BaseListResponse):
    SUB_MODEL = Deposit
