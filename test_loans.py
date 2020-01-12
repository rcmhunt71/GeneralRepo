import unittest

from PRICE.APIs.loans.models.add_loan_data import (
    AddLoanDataColEntryKeys, AddLoanRowValueKeys, AddLoanDataTableKeys, AddLoanDataColEntry, AddLoanDataCols,
    AddLoanValueEntry, AddLoanRowColsValue, AddLoanRowColKeys, AddLoanRowEntry, AddLoanRowList, AddLoanDataTable)
from PRICE.APIs.loans.models.final_value import FinalValueFieldsKeys, FinalValueScreenKeys
from PRICE.APIs.loans.models.loan_detail_data import LoanDetailDataTableKeys
from PRICE.APIs.loans.responses.add_loan import AddLoanKeys, AddLoan
from PRICE.APIs.loans.responses.get_final_value_tags import GetFinalValueTags
from PRICE.APIs.loans.responses.get_loan import GetLoan
from PRICE.APIs.loans.responses.get_loan_detail import GetLoanDetail

from PRICE.APIs.loans.client import LoanClient

from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# ---------------------------------------------------------------
#     TEST DATA
# ---------------------------------------------------------------

# ================================================================
#     Client Info
# ================================================================
BASE_URL = "auto.test.pclender.dom"
DATABASE = "testset1"
PORT = 8080

# ================================================================
#     AddLoan Data
# ================================================================
LOAN_ID = "8675309"

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
column_headers = (("Loan_Number_ID", "Loan Number ID", "number"),
                  ("Status_ID", "Status ID", "number"),
                  ("Owner_Name", "Owner Name", "string"))


def build_add_loan_data_column(data_tuple):
    return {
        AddLoanDataColEntryKeys.ID: data_tuple[0],
        AddLoanDataColEntryKeys.LABEL: data_tuple[1],
        AddLoanDataColEntryKeys.TYPE: data_tuple[2],
    }


add_loan_data_columns_list = [build_add_loan_data_column(data) for data in column_headers]


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


# LOAN DETAILS
# TODO Need to finish building out data source for GetLoanDetails()

loan_detail_value_entry_1 = {AddLoanRowValueKeys.VALUE: "Bobby McFerrin"}
loan_detail_value_entry_2 = {AddLoanRowValueKeys.VALUE: 1}
loan_detail_value_entry_3 = {AddLoanRowValueKeys.VALUE: 10}

loan_detail_value_entry_4 = {AddLoanRowValueKeys.VALUE: "George Burns"}
loan_detail_value_entry_5 = {AddLoanRowValueKeys.VALUE: 2}
loan_detail_value_entry_6 = {AddLoanRowValueKeys.VALUE: 20}

loan_detail_value_entry_7 = {AddLoanRowValueKeys.VALUE: "Goose"}
loan_detail_value_entry_8 = {AddLoanRowValueKeys.VALUE: 3}
loan_detail_value_entry_9 = {AddLoanRowValueKeys.VALUE: 30}

loan_detail_col_values_list_1 = [loan_detail_value_entry_1, loan_detail_value_entry_2, loan_detail_value_entry_3]
loan_detail_col_values_list_2 = [loan_detail_value_entry_4, loan_detail_value_entry_5, loan_detail_value_entry_6]
loan_detail_col_values_list_3 = [loan_detail_value_entry_7, loan_detail_value_entry_8, loan_detail_value_entry_9]

loan_detail_col_value_dict_1 = {AddLoanRowColKeys.COL: loan_detail_col_values_list_1}
loan_detail_col_value_dict_2 = {AddLoanRowColKeys.COL: loan_detail_col_values_list_2}
loan_detail_col_value_dict_3 = {AddLoanRowColKeys.COL: loan_detail_col_values_list_3}

loan_detail_row_datum_1 = [loan_detail_col_value_dict_1, loan_detail_col_value_dict_2, loan_detail_col_value_dict_3]

loan_detail_data_table = {AddLoanDataTableKeys.COLS: add_loan_data_columns_list,
                          AddLoanDataTableKeys.ROWS: loan_detail_row_datum_1}


# ---------------------------------------------------------------
#     ADD LOAN TESTS
# ---------------------------------------------------------------
class TestAddLoans(unittest.TestCase, CommonResponseValidations):
    def test_add_loans_response(self):
        add_loan_args = response_args.copy()
        add_loan_args[AddLoanKeys.NEW_LOAN_NUMBER_ID] = LOAN_ID
        add_loan_response = AddLoan(**add_loan_args)

        # Verify response contains correct common data + added tags
        self._validate_response(model=add_loan_response, model_data=add_loan_args)


class TestGetFinalValueTags(unittest.TestCase, CommonResponseValidations):
    def test_get_final_value_response(self):
        fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)

        # Verify FinalValue tags are in model
        for attr, attr_data_list in fv_data:
            self._verify(
                descript=f"{fb_tags_resp.model_name}: Model has '{attr}' attribute",
                actual=hasattr(fb_tags_resp, attr), expected=True)

            self._verify(
                descript=f"{fb_tags_resp.model_name}: Attribute '{attr}' are identical",
                actual=getattr(fb_tags_resp, attr), expected=attr_data_list)

        # Verify response contains correct common data
        self._validate_response(model=fb_tags_resp, model_data=get_fv_tags_args)

    def test_get_final_value_fields_response_method(self):
        key = FinalValueFieldsKeys.FINAL_VALUE_FIELD
        fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)
        self._verify(
            descript=f"{fb_tags_resp.model_name}: '{key}' lists are identical",
            actual=getattr(fb_tags_resp, key), expected=fb_tags_resp.get_final_value_fields())

    def test_get_final_value_screen_response_method(self):
        key = FinalValueScreenKeys.FINAL_VALUE_SCREEN
        fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)
        self._verify(
            descript=f"{fb_tags_resp.model_name}: '{key}' lists are identical",
            actual=getattr(fb_tags_resp, key), expected=fb_tags_resp.get_final_value_screens())


class TestAddLoanData(unittest.TestCase, CommonResponseValidations):
    def test_AddLoanDataColEntry_model(self):
        index = 0
        data_col_resp = AddLoanDataColEntry(**add_loan_data_columns_list[index])
        self._validate_response(model=data_col_resp, model_data=add_loan_data_columns_list[index])

    def test_AddLoanDataCols_model(self):
        dc_cols_resp = AddLoanDataCols(*add_loan_data_columns_list)

        self._verify(
            descript=f"{dc_cols_resp.model_name}: Num of data column elements are equal",
            actual=len(dc_cols_resp), expected=len(add_loan_data_columns_list))

        for index, col_header_model in enumerate(dc_cols_resp):
            self._validate_response(model=col_header_model, model_data=add_loan_data_columns_list[index])

    def test_AddLoanValueEntry_model(self):
        val_resp_model = AddLoanValueEntry(**add_loan_value_entry_2)
        self._validate_response(model=val_resp_model, model_data=add_loan_value_entry_2)

    def test_AddLoanRowColValue_model(self):
        val_col_resp_model = AddLoanRowColsValue(*add_loan_col_values_list_1)

        self._verify(
            descript=f"{val_col_resp_model.model_name}: Num of col_value elements match data",
            actual=len(val_col_resp_model), expected=len(add_loan_col_values_list_1))

        for index, row_value_model in enumerate(val_col_resp_model):
            self._validate_response(model=row_value_model, model_data=add_loan_col_values_list_1[index])

    def test_AddLoanRowEntry_model(self):
        # Get the data keyword to be added to the response
        key = AddLoanRowEntry.ADD_KEYS[0]
        val_col_dict_resp = AddLoanRowEntry(**add_loan_col_value_dict_1)

        self._verify(
            descript=f"{val_col_dict_resp.model_name}: Num of '{key}' elements are equal",
            actual=len(getattr(val_col_dict_resp, key)),
            expected=len(add_loan_col_values_list_1))

        self._validate_response(model=val_col_dict_resp, model_data=add_loan_col_value_dict_1)

    def test_AddLoanRowList_model(self):
        row_data_resp = AddLoanRowList(*add_loan_row_datum_1)
        self._verify(
            descript=f"{row_data_resp.model_name}: Num of col_value elements match data",
            actual=len(row_data_resp), expected=len(add_loan_row_datum_1))

        for index, row_data_model in enumerate(row_data_resp):
            self._validate_response(model=row_data_model, model_data=add_loan_row_datum_1[index])

    def test_AddLoanDataTable_response(self):
        data_table_resp = AddLoanDataTable(**add_loan_data_table)

        for attr in [AddLoanDataTableKeys.ROWS, AddLoanDataTableKeys.COLS]:
            self._verify(
                descript=f"{data_table_resp.model_name}: Has attribute '{attr}'",
                actual=hasattr(data_table_resp, attr), expected=True)

        self._validate_response(model=data_table_resp, model_data=add_loan_data_table)


class TestGetLoan(unittest.TestCase, CommonResponseValidations):
    def test_GetLoan_response(self):
        get_loan_data = response_args.copy()
        get_loan_data[AddLoanDataTableKeys.DATA_TABLE] = add_loan_data_table
        get_loan_resp = GetLoan(**get_loan_data)

        attr = AddLoanDataTableKeys.DATA_TABLE
        self._verify(descript=f"{get_loan_resp.model_name}: has '{attr}'",
                     actual=hasattr(get_loan_resp, attr), expected=True)

        sub_model = getattr(get_loan_resp, attr)
        for attr in [AddLoanDataTableKeys.ROWS, AddLoanDataTableKeys.COLS]:
            self._verify(
                descript=f"{get_loan_resp.model_name}: has attribute '{attr}'",
                actual=hasattr(sub_model, attr), expected=True)

        self._validate_response(model=get_loan_resp, model_data=get_loan_data)

    @unittest.skip(reason="Need to fix data supporting underlying model.")
    def test_GetLoanDetail_response(self):
        get_loan_detail_data = response_args.copy()
        get_loan_detail_data[AddLoanDataTableKeys.DATA_TABLE] = add_loan_data_table
        get_loan_resp = GetLoanDetail(**get_loan_detail_data)

        # ERROR: Need to address that basic row element is different than add_loan_data table element.

        attr = LoanDetailDataTableKeys.DATA_TABLE
        self._verify(descript=f"{get_loan_resp.model_name}: has '{attr}'",
                     actual=hasattr(get_loan_resp, attr), expected=True)

        sub_model = getattr(get_loan_resp, attr)
        for attr in [LoanDetailDataTableKeys.ROWS, LoanDetailDataTableKeys.COLS]:
            self._verify(
                descript=f"{get_loan_resp.model_name}: has attribute '{attr}'",
                actual=hasattr(sub_model, attr), expected=True)

        self._validate_response(model=get_loan_resp, model_data=get_loan_detail_data)


class TestLoanClient(unittest.TestCase, CommonResponseValidations):
    def test_AddLoan_client(self):
        # Build mock data to insert into client response
        add_loan_args = response_args.copy()
        add_loan_args[AddLoanKeys.NEW_LOAN_NUMBER_ID] = LOAN_ID

        # Use client to make call
        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=add_loan_args)

        # Make and validate client call
        response_model = client.add_loan(session_id="123456789", nonce="DEADBEEF15DECEA5ED")
        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=add_loan_args)


if __name__ == '__main__':
    unittest.main()
