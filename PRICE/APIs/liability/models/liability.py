from dataclasses import dataclass

from PRICE.base.abstract.base_response import BaseResponse, BaseListResponse


@dataclass
class LiabilityEntryKeys:
    LIABILITY_ID: str = "LiabilityID"
    CUSTOMER_ID: str = "CustomerID"
    INSTITUTION_ID: str = "InstitutionID"
    LIABILITY_TYPE: str = "LiabilityType"
    ACCOUNT_NAME: str = "AccountName"
    ACCOUNT_NUMBER: str = "AccountNumber"
    BALANCE: str = "Balance"
    TERM: str = "Term"
    PAYMENT: str = "Payment"
    PAYOFF: str = "Payoff"
    TO_BE_PAID_OFF: str = "ToBePaidOff"


@dataclass
class LiabilitiesKeys:
    LIABILITIES: str = "Liabilities"


@dataclass
class AddLiabilityKeys:
    LIABILITY_ID: str = "LiabilityID"


class LiabilityEntry(BaseResponse):
    ADD_KEYS = [LiabilityEntryKeys.LIABILITY_ID, LiabilityEntryKeys.CUSTOMER_ID, LiabilityEntryKeys.INSTITUTION_ID,
                LiabilityEntryKeys.LIABILITY_TYPE, LiabilityEntryKeys.ACCOUNT_NAME, LiabilityEntryKeys.ACCOUNT_NUMBER,
                LiabilityEntryKeys.BALANCE, LiabilityEntryKeys.TERM, LiabilityEntryKeys.PAYMENT,
                LiabilityEntryKeys.PAYOFF, LiabilityEntryKeys.TO_BE_PAID_OFF]

    SUB_MODELS = [None for _ in range(len(ADD_KEYS))]


class LiabilityEntriesList(BaseListResponse):
    SUB_MODEL = LiabilityEntry
