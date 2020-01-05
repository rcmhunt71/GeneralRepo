import unittest

from PRICE.loans.models.loan_status import LoanStatusKeys, LoanStatus, LoanStatuses
from PRICE.loans.responses.get_loan_statuses import GetLoanStatuses
from PRICE.logger.logging import Logger
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

log = Logger()

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
            self._verify(
                descript=f"{loan_status_obj.model_name}: '{key}' attributes are identical",
                actual=getattr(loan_status_obj, key), expected=status_data_1[key])

    def test_loan_statuses_model(self):
        loan_statuses_obj = LoanStatuses(*statuses_data)
        self._validate_loan_model(model=loan_statuses_obj, keys=status_data_1.keys())

    def test_get_loan_status_response(self):
        loan_status_resp = GetLoanStatuses(**full_status_data)
        self._verify(
            descript=f"{loan_status_resp.model_name}: '{LoanStatusKeys.LOAN_STATUSES}' attribute is defined",
            actual=hasattr(loan_status_resp, LoanStatusKeys.LOAN_STATUSES), expected=True)

        loan_status_model = getattr(loan_status_resp, LoanStatusKeys.LOAN_STATUSES)

        self._validate_loan_model(model=loan_status_model, keys=status_data_1.keys())
        self._validate_response(model=loan_status_resp, model_data=full_status_data)

    def _validate_loan_model(self, model, keys):
        for elem in range(len(statuses_data)):
            for key in keys:
                self._verify(
                    descript=f"{model.model_name} (Element #{elem}): '{key}' attributes are identical",
                    actual=getattr(model[elem], key), expected=statuses_data[elem][key])


if __name__ == "__main__":
    unittest.main()
