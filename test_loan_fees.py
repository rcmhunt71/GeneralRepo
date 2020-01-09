import unittest
from random import randrange, choice

from PRICE.APIs.fees.models.loan_fees import LoanFeeColumnEntry, LoanFeeColumnEntryKeys, LoanFeeColumnEntryList
from PRICE.tests.common_response_args import CommonResponseValidations

NUMBER_COLUMN_ENTRIES = 4

column_entry_data = {
    LoanFeeColumnEntryKeys.LABEL: ["Loan Number ID", "Fee ID", "Random ID"],
    LoanFeeColumnEntryKeys.TYPE: ["number", "text", "xml"]
}


def build_loan_fee_column_entry():
    return {
        LoanFeeColumnEntryKeys.ID: randrange(999),
        LoanFeeColumnEntryKeys.LABEL: choice(column_entry_data[LoanFeeColumnEntryKeys.LABEL]),
        LoanFeeColumnEntryKeys.TYPE: choice(column_entry_data[LoanFeeColumnEntryKeys.TYPE]),
    }


column_entries = [build_loan_fee_column_entry() for _ in range(NUMBER_COLUMN_ENTRIES)]


class TestGetLoanFeesColumns(unittest.TestCase, CommonResponseValidations):
    def test_loan_fee_column_entry_model(self):
        elem = randrange(NUMBER_COLUMN_ENTRIES)
        model = LoanFeeColumnEntry(**column_entries[elem])
        self._validate_response(model=model, model_data=column_entries[elem])

    def test_loan_fee_column_list(self):
        model = LoanFeeColumnEntryList(*column_entries)
        self._verify(descript=f"{model.model_name}: has correct number of elements",
                     actual=len(model), expected=len(column_entries))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=column_entries[index])


if __name__ == '__main__':
    unittest.main()
