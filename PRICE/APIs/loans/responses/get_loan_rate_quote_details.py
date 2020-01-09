from PRICE.APIs.loans.models.rate_quote_details import RateQuoteDetailsInfoKeys, RateQuoteDetails
from PRICE.base.common.response import CommonResponse


class GetLoanRateQuoteDetails(CommonResponse):
    ADD_KEYS = [RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS]
    SUB_MODELS = [RateQuoteDetails]
