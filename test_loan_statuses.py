import unittest

from PRICE.loans.models.loan_status import LoanStatusKeys, LoanStatus, LoanStatuses
from PRICE.loans.responses.get_loan_statuses import GetLoanStatuses
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# --------------------------------------------------
#             LOAN STATUS TEST DATA
# --------------------------------------------------

status_data_1 = {
    LoanStatusKeys.F_LOAN_NUMBER_ID: 2546,
    LoanStatusKeys.F_LOAN_STATUS: "Application",
}

status_data_2 = {
    LoanStatusKeys.F_LOAN_NUMBER_ID: 8675309,
    LoanStatusKeys.F_LOAN_STATUS: "Denied",
}

status_data_3 = {
    LoanStatusKeys.F_LOAN_NUMBER_ID: 55884466,
    LoanStatusKeys.F_LOAN_STATUS: "Approved",
}

statuses_data = [status_data_1, status_data_2, status_data_3]

full_status_data = response_args.copy()
full_status_data[LoanStatusKeys.LOAN_STATUSES] = statuses_data


# --------------------------------------------------
#             LOAN STATUS TESTS
# --------------------------------------------------
class TestLoanStatus(unittest.TestCase, CommonResponseValidations):
    def test_loan_status_model(self):
        loan_status_obj = LoanStatus(**status_data_1)
        for key in status_data_1.keys():
            self.assertEqual(getattr(loan_status_obj, key), status_data_1[key])

    def test_loan_statuses_model(self):
        loan_statuses_obj = LoanStatuses(*statuses_data)
        self._validate_loan_model(model=loan_statuses_obj, keys=status_data_1.keys())

    def test_get_loan_status_response(self):
        loan_status_resp = GetLoanStatuses(**full_status_data)
        self.assertTrue(hasattr(loan_status_resp, LoanStatusKeys.LOAN_STATUSES))

        loan_status_model = getattr(loan_status_resp, LoanStatusKeys.LOAN_STATUSES)

        self._validate_loan_model(model=loan_status_model, keys=status_data_1.keys())
        self._validate_response(model=loan_status_resp, model_data=full_status_data)

    def _validate_loan_model(self, model, keys):
        for elem in range(len(statuses_data)):
            for key in keys:
                self.assertEqual(getattr(model[elem], key), statuses_data[elem][key])


if __name__ == "__main__":
    unittest.main()
