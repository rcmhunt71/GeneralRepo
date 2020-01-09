import unittest
from random import randrange, choice

from PRICE.APIs.fees.models.loan_fees import (LoanFeeColumnEntry, LoanFeeColumnEntryKeys, LoanFeeColumnEntryList,
                                              LoanFeeRowEntryKeys, LoanFeeRowEntry, LoanFeeRowEntryList,
                                              LoanFeeRowColEntryKey, LoanFeeRowCol, LoanFeeRowColList,
                                              LoanFeeKeys, LoanFeeRowKeys, LoanFeeColumnKeys, LoanFees)
from PRICE.APIs.fees.responses.get_loan_fees import GetLoanFees
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# ========================================
# ============ TEST DATA =================
# ========================================
NUMBER_COLUMN_ENTRIES = 3
NUMBER_ROW_ENTRIES = 8

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


def build_loan_fee_row_entry():
    return {
        LoanFeeRowEntryKeys.VALUE: randrange(100)
    }


column_entries = [build_loan_fee_column_entry() for _ in range(NUMBER_COLUMN_ENTRIES)]
row_entries = [build_loan_fee_row_entry() for _ in range(NUMBER_ROW_ENTRIES)]
row_col_dict_data = {LoanFeeRowColEntryKey.COL: row_entries}
row_col_list_data = [{LoanFeeRowColEntryKey.COL: [build_loan_fee_row_entry() for _ in range(NUMBER_ROW_ENTRIES)]}
                     for _ in range(NUMBER_COLUMN_ENTRIES)]
fee_response_data = {
    LoanFeeColumnKeys.COLS: column_entries,
    LoanFeeRowKeys.ROWS: row_col_list_data,
}

# ========================================
# ================ TESTS =================
# ========================================


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


class TestGetLoanFeesRows(unittest.TestCase, CommonResponseValidations):
    def test_loan_fee_row_entry_model(self):
        row_index = randrange(NUMBER_ROW_ENTRIES)
        row_entry_model = LoanFeeRowEntry(**row_entries[row_index])
        self._validate_response(model=row_entry_model, model_data=row_entries[row_index])

    def test_loan_fee_row_list(self):
        model = LoanFeeRowEntryList(*row_entries)
        self._verify(descript=f"{model.model_name}: has correct number of elements",
                     actual=len(model), expected=len(row_entries))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=row_entries[index])

    def test_loan_row_col_model(self):
        model = LoanFeeRowCol(**row_col_dict_data)
        self._validate_response(model=model, model_data=row_col_dict_data)

    def test_loan_row_col_list_model(self):
        model = LoanFeeRowColList(*row_col_list_data)
        self._verify(f"{model.model_name}: has correct number of elements",
                     actual=len(model), expected=len(row_col_list_data))

    def test_loan_fees_model(self):
        data = {
            LoanFeeColumnKeys.COLS: column_entries,
            LoanFeeRowKeys.ROWS: row_col_list_data
        }
        model = LoanFees(**data)
        self._validate_response(model=model, model_data=data)


class TestGetLoanResponse(unittest.TestCase, CommonResponseValidations):
    def test_GetLoanFees_response(self):
        fee_data = response_args.copy()
        fee_data[LoanFeeKeys.LOAN_FEES] = fee_response_data
        get_loan_fees_response = GetLoanFees(**fee_data)
        self._validate_response(model=get_loan_fees_response, model_data=fee_data)


if __name__ == '__main__':
    unittest.main()
