import typing
import unittest

from APIs.loans.client import LoanClient
from APIs.loans.requests.set_loan_rate_quote_data import SetLoanRateQuoteDataKeys, SetLoanRateQuoteDataPayload
from tests.common_request_utils import RequestValidationTools
from tests.common_response_args import CommonResponseValidations, response_args


# ================================================================
#     Client Info
# ================================================================
BASE_URL = "auto.test.pclender.dom"
DATABASE = "testset1"
PORT = 8080


SESSION_ID = 123456789
NONCE = "DEADBEEF15DECEA5ED"
LOAN_NUMBER_ID = "45678524663"
VENDOR_NAME = "1234567890"

set_loan_rate_quote_args = {
    "coverage": "This is a coverage --> here",
    "rate_quote_id": 34537349857,
    "status_description": "This is the status_description",
}


def _build_payload(args_dict: typing.Dict[str, typing.Any]) -> typing.Dict[
    str, typing.List[typing.Dict[str, typing.Any]]]:
    """
    Build the expected payload format based on the data provided into the requesting client call.

    :param args_dict: Dictionary of the payload data arguments
    :return: Dict of lists of key/value dicts (data)
    """
    return {SetLoanRateQuoteDataKeys.LOAN_RATE_QUOTE_DETAILS:
                [{SetLoanRateQuoteDataKeys.FIELD_NAME: getattr(SetLoanRateQuoteDataPayload, key.upper()),
                  SetLoanRateQuoteDataKeys.FIELD_VALUE: value} for key, value in args_dict.items()]}


class TestSetLoanRateQuoteData(unittest.TestCase, RequestValidationTools, CommonResponseValidations):

    def test_SetLoanRateQuoteData_client_with_kwargs(self) -> typing.NoReturn:
        # Build mock data to insert into client response
        set_loan_data_quote_data_response = response_args.copy()

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=set_loan_data_quote_data_response)

        # Make and validate client call
        response_model = client.set_loan_rate_quote_data(
            session_id=SESSION_ID, nonce=NONCE, loan_number_id=LOAN_NUMBER_ID,
            vendor_name=VENDOR_NAME, **set_loan_rate_quote_args)

        # Validation
        self.validate_payload(expected_dict=_build_payload(set_loan_rate_quote_args), actual_dict=client.payload)
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=set_loan_data_quote_data_response)

    def test_SetLoanRateQuoteData_client_with_payload(self) -> typing.NoReturn:
        # Build mock data to insert into client response
        set_loan_data_quote_data_response = response_args.copy()

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=set_loan_data_quote_data_response)

        # Make and validate client call
        response_model = client.set_loan_rate_quote_data(
            session_id=SESSION_ID, nonce=NONCE, loan_number_id=LOAN_NUMBER_ID,
            vendor_name=VENDOR_NAME, payload_dict=_build_payload(args_dict=set_loan_rate_quote_args))

        # Validation
        self.validate_payload(expected_dict=_build_payload(set_loan_rate_quote_args), actual_dict=client.payload)
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=set_loan_data_quote_data_response)


if __name__ == "__main__":
    unittest.main()
