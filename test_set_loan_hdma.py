import typing
import unittest

from APIs.loans.client import LoanClient
from APIs.loans.requests.set_loan_hmda import SetLoanHDMAPayload, SetLoanHDMADataKeys
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
MSA = "HDMA MSA"
CENSUS = "HMDA Census Data"
OVERRIDE = True
REASON_1 = "Because you are broke"
REASON_2 = "Because the property is overvalued"

prebuilt_payload = {
    "hmda_msa": MSA,
    "hmda_census": CENSUS,
    "hmda_2018_loan_purpose_override": OVERRIDE,
    "hmda_2018_denial_reason_1": REASON_1,
    "hmda_2018_denial_reason_2": REASON_2,
}


def _build_payload() -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
    """
    Build the expected payload format based on the data provided into the requesting client call.

    :return: Dict of lists of key/value dicts (data)
    """
    return {SetLoanHDMADataKeys.LOAN_HDMA_FIELDS:
                [{SetLoanHDMADataKeys.FIELD_NAME: getattr(SetLoanHDMAPayload, key.upper()),
                  SetLoanHDMADataKeys.FIELD_VALUE: value} for key, value in prebuilt_payload.items()]}


class TestSetLoanData(unittest.TestCase, RequestValidationTools, CommonResponseValidations):
    def test_SetLoanHDMA_client(self) -> typing.NoReturn:
        # Build mock data to insert into client response
        set_loan_data_response = response_args.copy()

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=set_loan_data_response)

        # Make and validate client call
        response_model = client.set_loan_hdma(session_id=SESSION_ID, nonce=NONCE, loan_number_id=LOAN_NUMBER_ID,
                                              **prebuilt_payload)

        # Validation
        self.validate_payload(expected_dict=_build_payload(), actual_dict=client.payload)
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=set_loan_data_response)


if __name__ == "__main__":
    unittest.main()
