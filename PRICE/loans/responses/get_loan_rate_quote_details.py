from PRICE.common.response import CommonResponse
from PRICE.loans.models.rate_quote_details import RateQuoteDetailsInfoKeys, RateQuoteDetails


class GetLoanRateQuoteDetails(CommonResponse):
    ADD_KEYS = [RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS]
    SUB_MODELS = [RateQuoteDetails]
