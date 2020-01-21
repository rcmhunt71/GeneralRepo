import unittest

from APIs.loans.client import LoanClient
from APIs.loans.requests.set_anti_steering_data import SetAntiSteeringDataKeys
from tests.common_request_utils import RequestValidationTools
from tests.common_response_args import CommonResponseValidations, response_args


# ================================================================
#     Client Info
# ================================================================
BASE_URL = "auto.test.pclender.dom"
DATABASE = "testset1"
PORT = 8080


# ------------ DATA --------------
RATE = 0.04
BASE_LOAN_AMOUNT = 100000
OTHER_FINANCING = False

prebuilt_payload = {
    "rate": RATE,
    "base_loan_amount": BASE_LOAN_AMOUNT,
    "other_financing": OTHER_FINANCING,
}


class TestSetAntiSteeringDataClient(unittest.TestCase, CommonResponseValidations, RequestValidationTools):
    def test_AntiSteeringData_client_payload_as_args(self):
        # Build mock data to insert into client response
        set_anti_steering_data_args = response_args.copy()

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=set_anti_steering_data_args)

        # Make and validate client call
        response_model = client.set_anti_steering_data(session_id="123456789", nonce="DEADBEEF15DECEA5ED", rate=RATE,
                                                       loan_number_id="12345679", base_loan_amount=BASE_LOAN_AMOUNT,
                                                       other_financing=OTHER_FINANCING)

        self.validate_payload(expected_dict=prebuilt_payload, actual_dict=client.payload)
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=set_anti_steering_data_args)

    def test_AntiSteeringData_client_with_prebuilt_payload(self):
        # Build mock data to insert into client response
        set_anti_steering_data_args = response_args.copy()

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=set_anti_steering_data_args)

        # Make and validate client call
        response_model = client.set_anti_steering_data(session_id="123456789", nonce="DEADBEEF15DECEA5ED", rate=RATE,
                                                       loan_number_id="12345679", payload_dict=prebuilt_payload)

        self.validate_payload(expected_dict=prebuilt_payload, actual_dict=client.payload)
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=set_anti_steering_data_args)


if __name__ == "__main__":
    unittest.main()
