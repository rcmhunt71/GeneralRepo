from PRICE.APIs.fees.models.loan_fees import LoanFees, LoanFeeKeys
from PRICE.base.common.response import CommonResponse


class GetLoanFees(CommonResponse):
    ADD_KEYS = [LoanFeeKeys.LOAN_FEES]
    SUB_MODELS = [LoanFees]
