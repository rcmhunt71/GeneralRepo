import typing
import unittest

from APIs.loans.client import LoanClient
from APIs.loans.requests.set_loan_data import SetLoanDataKeys, SetLoanDataPayload
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
RATE = 0.04
BASE_LOAN_AMOUNT = 100000
RELOCATION = True
FLOOD_ZONE = False
LOCK_ID = "1234-4567"
TITLE_CONTACT_ID = 123456
TITLE_COMPANY_ID = 88667799
LOAN_PROCESSOR_ID = 8675309
LOAN_UNDERWRITER_ID = 10000001

prebuilt_payload = {
    "flood_zone": FLOOD_ZONE,
    "lock_type_id": LOCK_ID,
    "relocation": RELOCATION,
    "title_contact_id": TITLE_CONTACT_ID,
    "title_company_id": TITLE_COMPANY_ID,
    "loan_processor_id": LOAN_PROCESSOR_ID,
    "loan_underwriter_id": LOAN_UNDERWRITER_ID,
}


def _build_payload(args_dict: typing.Dict[str, typing.Any]) -> typing.Dict[
    str, typing.List[typing.Dict[str, typing.Any]]]:
    """
    Build the expected payload format based on the data provided into the requesting client call.

    :param args_dict: Dictionary of the payload data arguments
    :return: Dict of lists of key/value dicts (data)
    """
    return {SetLoanDataKeys.LOAN_FIELDS:
                [{SetLoanDataKeys.FIELD_NAME: getattr(SetLoanDataPayload, key.upper()),
                  SetLoanDataKeys.FIELD_VALUE: value} for key, value in args_dict.items()]}


class TestSetLoanData(unittest.TestCase, RequestValidationTools, CommonResponseValidations):
    def test_SetLoanData_client(self) -> typing.NoReturn:
        # Build mock data to insert into client response
        set_loan_data_response = response_args.copy()

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=set_loan_data_response)

        # Make and validate client call
        response_model = client.set_loan_data(session_id=SESSION_ID, nonce=NONCE, loan_number_id=LOAN_NUMBER_ID,
                                              **prebuilt_payload)

        # Validation
        self.validate_payload(expected_dict=_build_payload(prebuilt_payload), actual_dict=client.payload)
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=set_loan_data_response)


if __name__ == "__main__":
    unittest.main()
