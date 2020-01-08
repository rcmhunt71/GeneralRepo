from dataclasses import dataclass

from base.abstract.base_response import BaseResponse


@dataclass
class RateQuoteDetailsInfoKeys:
    VENDOR: str = "Vendor"
    PAYMENT_PERIOD: str = "PaymentPeriod"
    RENEWAL_TYPE: str = "RenewalType"
    ZERO_DUE_AT_CLOSING: str = "ZeroDueAtClosing"
    REFUNDABLE: str = "Refundable"
    COVERAGE: str = "Coverage"
    PAYMENT_TYPE: str = "PaymentType"
    MIS_SPECIAL_DEAL: str = "MISSpecialDeal"
    RATE_QUOTE_ID: str = "RateQuoteID"
    RATE_PLAN_TYPE: str = "RatePlanType"
    STATUS_DESCRIPTION: str = "StatusDescription"
    LOAN_RATE_QUOTE_DETAILS: str = "LoanRateQuoteDetails"


class RateQuoteDetails(BaseResponse):
    def __init__(self, **kwargs):
        self._VARS = [
            RateQuoteDetailsInfoKeys.VENDOR, RateQuoteDetailsInfoKeys.PAYMENT_PERIOD,
            RateQuoteDetailsInfoKeys.RENEWAL_TYPE, RateQuoteDetailsInfoKeys.ZERO_DUE_AT_CLOSING,
            RateQuoteDetailsInfoKeys.REFUNDABLE, RateQuoteDetailsInfoKeys.COVERAGE,
            RateQuoteDetailsInfoKeys.PAYMENT_TYPE, RateQuoteDetailsInfoKeys.MIS_SPECIAL_DEAL,
            RateQuoteDetailsInfoKeys.RATE_QUOTE_ID, RateQuoteDetailsInfoKeys.RATE_PLAN_TYPE,
            RateQuoteDetailsInfoKeys.STATUS_DESCRIPTION]
        super().__init__(keys=self._VARS, **kwargs)
