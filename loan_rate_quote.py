from PRICE.common.models.stats import StatsKeys
from PRICE.common.models.version import VersionKeys
from PRICE.common.response import CommonResponseKeys
from PRICE.loans.models.rate_quote_details import RateQuoteDetailsInfoKeys
from PRICE.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetails


version_args = {
    VersionKeys.MAJOR_VERSION: 10,
    VersionKeys.MINOR_VERSION: 20,
    VersionKeys.BUILD: 30,
    VersionKeys.HOT_FIX: 40,
}

stats_args = {
    StatsKeys.TOTAL_DATABASE_TIME: 35,
    StatsKeys.TOTAL_SERVER_TIME: 25,
    StatsKeys.METHOD_TIME: 15,
    StatsKeys.LOSTIME: 5,
}

response_args = {
    CommonResponseKeys.SUCCESSFUL: True,
    CommonResponseKeys.ERROR_MESSAGE: "Ok",
    CommonResponseKeys.ERROR_CODE: 0,
    CommonResponseKeys.TAGS: "",
    CommonResponseKeys.VERSION: version_args,
    CommonResponseKeys.STATS: stats_args,
    CommonResponseKeys.NONCE: "DEADBEEF-01234",
    CommonResponseKeys.RESPONDER: "E406F3C0BA2DDE5348F99BC0089-1224",
}

rate_quote = {
    RateQuoteDetailsInfoKeys.VENDOR: "ARCH",
    RateQuoteDetailsInfoKeys.PAYMENT_PERIOD: "Monthly",
    RateQuoteDetailsInfoKeys.RENEWAL_TYPE: "Constant",
    RateQuoteDetailsInfoKeys.ZERO_DUE_AT_CLOSING: "Yes",
    RateQuoteDetailsInfoKeys.REFUNDABLE: "NotRefundable",
    RateQuoteDetailsInfoKeys.COVERAGE: "35",
    RateQuoteDetailsInfoKeys.PAYMENT_TYPE: "LenderPaid",
    RateQuoteDetailsInfoKeys.MIS_SPECIAL_DEAL: "",
    RateQuoteDetailsInfoKeys.RATE_QUOTE_ID: "",
    RateQuoteDetailsInfoKeys.RATE_PLAN_TYPE: "Split Prem .75",
    RateQuoteDetailsInfoKeys.STATUS_DESCRIPTION: "test_me",
}

rate_quote_data = response_args.copy()
rate_quote_data[RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS] = rate_quote

# --- TEST ---

rate_quote_obj = GetLoanRateQuoteDetails(**rate_quote_data)
print(rate_quote_obj.LoanRateQuoteDetails)

