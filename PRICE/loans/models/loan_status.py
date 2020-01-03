from dataclasses import dataclass

from PRICE.abstract.base_response import BaseResponse, BaseListResponse


@dataclass
class LoanStatusKeys:
    F_LOAN_NUMBER_ID: str = "FLoanNumberId"
    F_LOAN_STATUS: str = "FLoanStatus"
    LOAN_STATUSES: str = "LoanStatuses"


class LoanStatus(BaseResponse):
    def __init__(self, **kwargs):
        self._VARS = [LoanStatusKeys.F_LOAN_NUMBER_ID, LoanStatusKeys.F_LOAN_STATUS]
        super().__init__(keys=self._VARS, **kwargs)


class LoanStatuses(BaseListResponse):
    SUB_MODEL = LoanStatus
