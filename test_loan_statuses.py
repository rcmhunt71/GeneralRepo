import unittest
from random import randrange, choice

from PRICE.APIs.loans.client import LoanClient
from PRICE.APIs.loans.models.loan_status import LoanStatusKeys, LoanStatus, LoanStatuses
from PRICE.APIs.loans.requests.get_loan_statuses import GetLoanStatusesRequest
from PRICE.APIs.loans.responses.get_loan_statuses import GetLoanStatusesResponse
from PRICE.logger.logging import Logger
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

log = Logger()

# ================================================================
#     Client Info
# ================================================================
BASE_URL = "auto.test.pclender.dom"
DATABASE = "testset1"
PORT = 8080


# --------------------------------------------------
#             LOAN STATUS TEST DATA
# --------------------------------------------------

statuses = ["Applied", "Denied", "Approved"]
NUMBER_OF_DATA = 3


def build_status_data():
    return {
        LoanStatusKeys.F_LOAN_NUMBER_ID: randrange(999999),
        LoanStatusKeys.F_LOAN_STATUS: choice(statuses),
    }


statuses_data = [build_status_data() for _ in range(NUMBER_OF_DATA)]

full_status_data = response_args.copy()
full_status_data[LoanStatusKeys.LOAN_STATUSES] = statuses_data


# --------------------------------------------------
#             LOAN STATUS TESTS
# --------------------------------------------------
class TestLoanStatus(unittest.TestCase, CommonResponseValidations):
    def test_loan_status_model(self):
        loan_status_obj = LoanStatus(**statuses_data[0])
        for key in statuses_data[0].keys():
            self._verify(
                descript=f"{loan_status_obj.model_name}: '{key}' attributes are identical",
                actual=getattr(loan_status_obj, key), expected=statuses_data[0][key])

    def test_loan_statuses_model(self):
        loan_statuses_obj = LoanStatuses(*statuses_data)
        self._validate_loan_model(model=loan_statuses_obj, keys=statuses_data[0].keys())

    def test_get_loan_status_response(self):
        loan_status_resp = GetLoanStatusesResponse(**full_status_data)
        self._verify(
            descript=f"{loan_status_resp.model_name}: '{LoanStatusKeys.LOAN_STATUSES}' attribute is defined",
            actual=hasattr(loan_status_resp, LoanStatusKeys.LOAN_STATUSES), expected=True)

        loan_status_model = getattr(loan_status_resp, LoanStatusKeys.LOAN_STATUSES)

        self._validate_loan_model(model=loan_status_model, keys=statuses_data[0].keys())
        self._validate_response(model=loan_status_resp, model_data=full_status_data)

    def _validate_loan_model(self, model, keys):
        for elem in range(len(statuses_data)):
            for key in keys:
                self._verify(
                    descript=f"{model.model_name} (Element #{elem}): '{key}' attributes are identical",
                    actual=getattr(model[elem], key), expected=statuses_data[elem][key])


class TestGetLoanStatusesClient(unittest.TestCase, CommonResponseValidations):
    def test_GetLoanStatuses_client(self):
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=full_status_data)

        response_model = client.get_loan_statuses(
            session_id="1232465798", nonce="DEADBEEF15DECEA5ED", loan_number_id=f"{randrange(999999):06}")

        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=full_status_data)


if __name__ == "__main__":
    unittest.main()
