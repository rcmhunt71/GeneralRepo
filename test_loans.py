import unittest

from PRICE.loans.models.add_loan_data import (
    AddLoanDataColEntryKeys, AddLoanRowValueKeys, AddLoanDataTableKeys, AddLoanDataColEntry, AddLoanDataCols,
    AddLoanValueEntry, AddLoanRowColsValue, AddLoanRowColKeys)
from PRICE.loans.models.final_value import FinalValueFieldsKeys, FinalValueScreenKeys
from PRICE.loans.responses.add_loan import AddLoanKeys, AddLoan
from PRICE.loans.responses.get_final_value_tags import GetFinalValueTags
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# ---------------------------------------------------------------
#     TEST DATA
# ---------------------------------------------------------------

# ================================================================
#     AddLoan Data
# ================================================================
loan_id = "8675309"

# ================================================================
#     FinalValue Data
# ================================================================
final_screen_list = [1024]
final_fields_list = ['Test1', 'Test2']

fv_data = zip([FinalValueScreenKeys.FINAL_VALUE_SCREEN, FinalValueFieldsKeys.FINAL_VALUE_FIELD],
              [final_screen_list, final_fields_list])

# ================================================================
#     Build FinalValue Input arguments (get_fv_tags_args)
# ================================================================
get_fv_tags_args = response_args.copy()
for arg, data_list in fv_data:
    get_fv_tags_args[arg] = data_list

# ================================================================
#     Build Add Loan Column Data
# ================================================================
add_loan_data_column_args_1 = {
    AddLoanDataColEntryKeys.ID: "Loan_Number_ID",
    AddLoanDataColEntryKeys.LABEL: "Loan Number ID",
    AddLoanDataColEntryKeys.TYPE: "number",
}

add_loan_data_column_args_2 = {
    AddLoanDataColEntryKeys.ID: "Status_ID",
    AddLoanDataColEntryKeys.LABEL: "Status ID",
    AddLoanDataColEntryKeys.TYPE: "number",
}

add_loan_data_column_args_3 = {
    AddLoanDataColEntryKeys.ID: "Owner_Name",
    AddLoanDataColEntryKeys.LABEL: "Owner Name",
    AddLoanDataColEntryKeys.TYPE: "string",
}

add_loan_data_columns_list = [add_loan_data_column_args_3, add_loan_data_column_args_1, add_loan_data_column_args_2]

add_loan_value_entry_1 = {AddLoanRowValueKeys.VALUE: "Bobby McFerrin"}
add_loan_value_entry_2 = {AddLoanRowValueKeys.VALUE: 1}
add_loan_value_entry_3 = {AddLoanRowValueKeys.VALUE: 10}

add_loan_value_entry_4 = {AddLoanRowValueKeys.VALUE: "George Burns"}
add_loan_value_entry_5 = {AddLoanRowValueKeys.VALUE: 2}
add_loan_value_entry_6 = {AddLoanRowValueKeys.VALUE: 20}

add_loan_value_entry_7 = {AddLoanRowValueKeys.VALUE: "Goose"}
add_loan_value_entry_8 = {AddLoanRowValueKeys.VALUE: 3}
add_loan_value_entry_9 = {AddLoanRowValueKeys.VALUE: 30}

add_loan_col_values_list_1 = [add_loan_value_entry_1, add_loan_value_entry_2, add_loan_value_entry_3]
add_loan_col_values_list_2 = [add_loan_value_entry_4, add_loan_value_entry_5, add_loan_value_entry_6]
add_loan_col_values_list_3 = [add_loan_value_entry_7, add_loan_value_entry_8, add_loan_value_entry_9]

add_loan_col_value_dict_1 = {AddLoanRowColKeys.COL: add_loan_col_values_list_1}
add_loan_col_value_dict_2 = {AddLoanRowColKeys.COL: add_loan_col_values_list_2}
add_loan_col_value_dict_3 = {AddLoanRowColKeys.COL: add_loan_col_values_list_3}

add_loan_row_datum_1 = [add_loan_col_value_dict_1, add_loan_col_value_dict_2, add_loan_col_value_dict_3]

add_loan_data_table = {AddLoanDataTableKeys.COLS: add_loan_data_columns_list,
                       AddLoanDataTableKeys.ROWS: add_loan_row_datum_1}


# ---------------------------------------------------------------
#     ADD LOAN TESTS
# ---------------------------------------------------------------
class TestAddLoans(unittest.TestCase, CommonResponseValidations):
    def test_add_loans_response(self):
        add_loan_args = response_args.copy()
        add_loan_args[AddLoanKeys.NEW_LOAN_NUMBER_ID] = loan_id
        add_loan_response = AddLoan(**add_loan_args)

        # Verify response contains correct common data + added tags
        self._validate_response(model=add_loan_response, model_data=add_loan_args)


class TestGetFinalValueTags(unittest.TestCase, CommonResponseValidations):
    def test_get_final_value_response(self):
        fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)

        # Verify FinalValue tags are in model
        for attr, attr_data_list in fv_data:
            self.assertTrue(hasattr(fb_tags_resp, attr))
            self.assertListEqual(getattr(fb_tags_resp, attr), attr_data_list)

        # Verify response contains correct common data
        self._validate_response(model=fb_tags_resp, model_data=get_fv_tags_args)

    def test_get_final_value_fields_response_method(self):
        key = FinalValueFieldsKeys.FINAL_VALUE_FIELD
        fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)
        self.assertListEqual(getattr(fb_tags_resp, key), fb_tags_resp.get_final_value_fields())

    def test_get_final_value_screen_response_method(self):
        key = FinalValueScreenKeys.FINAL_VALUE_SCREEN
        fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)
        self.assertListEqual(getattr(fb_tags_resp, key), fb_tags_resp.get_final_value_screens())


class TestAddLoanData(unittest.TestCase, CommonResponseValidations):
    def test_AddLoanDataColEntry_model(self):
        data_col_resp = AddLoanDataColEntry(**add_loan_data_column_args_1)
        self._validate_response(model=data_col_resp, model_data=add_loan_data_column_args_1)

    def test_AddLoanDataCols_model(self):
        dc_cols_resp = AddLoanDataCols(*add_loan_data_columns_list)
        self.assertEqual(len(dc_cols_resp), len(add_loan_data_columns_list))
        for index, col_header_model in enumerate(dc_cols_resp):
            self._validate_response(model=col_header_model, model_data=add_loan_data_columns_list[index])

    def test_AddLoanValueEntry_model(self):
        val_resp_model = AddLoanValueEntry(**add_loan_value_entry_2)
        self._validate_response(model=val_resp_model, model_data=add_loan_value_entry_2)

    def test_AddLoanRowColValue_model(self):
        val_col_resp_model = AddLoanRowColsValue(*add_loan_col_values_list_1)
        self.assertEqual(len(val_col_resp_model), len(add_loan_col_values_list_1))
        for index, row_value_model in enumerate(val_col_resp_model):
            self._validate_response(model=row_value_model, model_data=add_loan_col_values_list_1[index])


if __name__ == '__main__':
    unittest.main()