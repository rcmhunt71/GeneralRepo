from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class LoanStatusKeys:
    F_LOAN_NUMBER_ID: str = "FLoanNumberId"
    F_LOAN_STATUS: str = "FLoanStatus"
    LOAN_STATUSES: str = "LoanStatuses"


class LoanStatus(BaseResponse):
    ADD_KEYS = [LoanStatusKeys.F_LOAN_NUMBER_ID, LoanStatusKeys.F_LOAN_STATUS]
    SUB_MODELS = [None, None]


class LoanStatuses(BaseListResponse):
    SUB_MODEL = LoanStatus
