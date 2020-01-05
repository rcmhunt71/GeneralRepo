import unittest

from PRICE.loans.models.rate_quote_details import RateQuoteDetailsInfoKeys
from PRICE.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetails
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# --------------------------------------------------
#             RATE QUOTE TEST DATA
# --------------------------------------------------

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


# --------------------------------------------------
#             RATE QUOTE TEST
# --------------------------------------------------
class TestRateQuote(unittest.TestCase, CommonResponseValidations):
    def test_rate_quote_response(self):
        rate_quote_data = response_args.copy()
        rate_quote_data[RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS] = rate_quote

        rate_quote_obj = GetLoanRateQuoteDetails(**rate_quote_data)
        self.assertTrue(hasattr(rate_quote_obj, RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS))

        model = getattr(rate_quote_obj, RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS)

        self._validate_model(model=model, keys=rate_quote.keys())
        self._validate_response(model=rate_quote_obj, model_data=rate_quote_data)

    def _validate_model(self, model, keys):
        for key in keys:
            self._verify(
                descript=f"{model.model_name}: '{key}' values are equal",
                actual=getattr(model, key), expected=rate_quote[key])

            # self.assertEqual(getattr(model, key), rate_quote[key])


if __name__ == '__main__':
    unittest.main()
