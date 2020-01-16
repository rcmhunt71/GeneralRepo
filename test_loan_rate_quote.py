from random import randrange
import unittest

from APIs.loans.client import LoanClient
from APIs.loans.models.rate_quote_details import RateQuoteDetailsInfoKeys
from APIs.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetailsResponse
from PRICE.tests.common_response_args import CommonResponseValidations, response_args


# ================================================================
#     Client Info
# ================================================================
BASE_URL = "auto.test.pclender.dom"
DATABASE = "testset1"
PORT = 8080


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

        rate_quote_obj = GetLoanRateQuoteDetailsResponse(**rate_quote_data)
        self.assertTrue(hasattr(rate_quote_obj, RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS))

        model = getattr(rate_quote_obj, RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS)

        self._validate_model(model=model, keys=rate_quote.keys())
        self._validate_response(model=rate_quote_obj, model_data=rate_quote_data)

    def _validate_model(self, model, keys):
        for key in keys:
            self._verify(
                descript=f"{model.model_name}: '{key}' values are equal",
                actual=getattr(model, key), expected=rate_quote[key])


class TestRateQuoteDetailsClient(unittest.TestCase, CommonResponseValidations):
    def test_GetLoanRateQuoteDetails_client(self):
        rate_quote_data = response_args.copy()
        rate_quote_data[RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS] = rate_quote

        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=rate_quote_data)

        response_model = client.get_loan_rate_quote_details(
            session_id="1232465798", nonce="DEADBEEF15DECEA5ED", loan_number_id=f"{randrange(999999):06}")

        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=rate_quote_data)


if __name__ == '__main__':
    unittest.main()
