from PRICE.APIs.loans.models.loan_status import LoanStatusKeys, LoanStatuses
from PRICE.base.common.response import CommonResponse


class GetLoanStatusesResponse(CommonResponse):
    ADD_KEYS = [LoanStatusKeys.LOAN_STATUSES]
    SUB_MODELS = [LoanStatuses]
