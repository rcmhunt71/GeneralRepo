#!/usr/bin/env python

from PRICE.common.response import CommonResponseKeys
from PRICE.configuration.configuration_list import ConfigurationList, ConfigurationListKeys
from PRICE.loans.models.add_loan_data import (
    AddLoanDataColEntryKeys, AddLoanRowValueKeys, AddLoanDataTableKeys, AddLoanRowColKeys, AddLoanRowEntry, AddLoanRowList, AddLoanDataTable)
from PRICE.loans.models.loan_detail_data import (
    LoanDetailColEntryKeys, LoanDetailRowValueKeys, LoanDetailDataTableKeys, LoanDetailRowColKeys)
from PRICE.loans.responses.get_loan import GetLoan
from PRICE.loans.responses.get_loan_detail import GetLoanDetail
from PRICE.tests.common_response_args import response_args

# ---------------------------------------------------------------
#     TEST DATA
# ---------------------------------------------------------------

config_list = [
    "Mr.",
    "Mrs.",
    "Ms.",
    "Miss",
    "Dr.",
]

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

loan_detail_data_column_args_1 = {
    LoanDetailColEntryKeys.ID: "Loan_Number_ID",
    LoanDetailColEntryKeys.TYPE: "number",
}

loan_detail_data_column_args_2 = {
    LoanDetailColEntryKeys.ID: "Status_ID",
    LoanDetailColEntryKeys.TYPE: "number",
}

loan_detail_data_column_args_3 = {
    LoanDetailColEntryKeys.ID: "Owner_Name",
    LoanDetailColEntryKeys.TYPE: "string",
}

loan_detail_data_columns_list = [loan_detail_data_column_args_3, loan_detail_data_column_args_1,
                                 loan_detail_data_column_args_2]

loan_detail_value_entry_1 = {LoanDetailRowValueKeys.VALUE: "Errol Flynn"}
loan_detail_value_entry_2 = {LoanDetailRowValueKeys.VALUE: 5}
loan_detail_value_entry_3 = {LoanDetailRowValueKeys.VALUE: 500}

loan_detail_value_entry_4 = {LoanDetailRowValueKeys.VALUE: "Burt Reynolds"}
loan_detail_value_entry_5 = {LoanDetailRowValueKeys.VALUE: 7}
loan_detail_value_entry_6 = {LoanDetailRowValueKeys.VALUE: 700}

loan_detail_value_entry_7 = {LoanDetailRowValueKeys.VALUE: "Maverick"}
loan_detail_value_entry_8 = {LoanDetailRowValueKeys.VALUE: 10}
loan_detail_value_entry_9 = {LoanDetailRowValueKeys.VALUE: 1000}

loan_detail_col_values_list_1 = [loan_detail_value_entry_1, loan_detail_value_entry_2, loan_detail_value_entry_3]
loan_detail_col_values_list_2 = [loan_detail_value_entry_4, loan_detail_value_entry_5, loan_detail_value_entry_6]
loan_detail_col_values_list_3 = [loan_detail_value_entry_7, loan_detail_value_entry_8, loan_detail_value_entry_9]

loan_detail_col_value_dict_1 = {LoanDetailRowColKeys.COL: loan_detail_col_values_list_1}
loan_detail_col_value_dict_2 = {LoanDetailRowColKeys.COL: loan_detail_col_values_list_2}
loan_detail_col_value_dict_3 = {LoanDetailRowColKeys.COL: loan_detail_col_values_list_3}

loan_detail_row_datum_1 = [loan_detail_col_value_dict_1, loan_detail_col_value_dict_2,
                           loan_detail_col_value_dict_3]

loan_detail_data_table = {LoanDetailDataTableKeys.COLS: loan_detail_data_columns_list,
                          LoanDetailDataTableKeys.ROWS: loan_detail_row_datum_1}


# ---------------------------------------------------------------
#   VALIDATION SECTION
# ---------------------------------------------------------------
config_args = response_args.copy()
config_args[ConfigurationListKeys.CONFIGURATION_LIST] = config_list
configuration = ConfigurationList(**config_args)
print(f"CONFIGURATION LIST:\n{configuration}")

key = AddLoanRowEntry.ADD_KEYS[0]
val_col_dict_resp = AddLoanRowEntry(**add_loan_col_value_dict_1)
print(f"COL DICT --> Key = '{key}':\n{getattr(val_col_dict_resp, key)}\n")

row_data_resp = AddLoanRowList(*add_loan_row_datum_1)
print(f"ROW COLUMN LIST DATA, FIRST ELEMENT:\n{row_data_resp[0].c}")
print(f"ROW COLUMN LIST DATA, SECOND ELEMENT:\n{row_data_resp[1].c}\n")

data_table_resp = AddLoanDataTable(**add_loan_data_table)
print(f"DATA LABEL: {data_table_resp.cols[1].id}")
print(f"DATA LABEL: {data_table_resp.rows[1].c[1].v}\n")




get_loan_data = response_args.copy()
get_loan_data[AddLoanDataTableKeys.DATA_TABLE] = add_loan_data_table
get_loan_resp = GetLoan(**get_loan_data)
print(f"VERSION: {get_loan_resp.Version.full_version_info()}")
print(f"get_loan_resp.Data.rows[0].c[1].v: {get_loan_resp.Data.rows[0].c[0].v}")
print(f"get_loan_resp.Data.rows[1].c[2].v: {get_loan_resp.Data.rows[1].c[0].v}\n")

get_loan_resp.show_data_table()
print(f"RAW STATS DATA: {getattr(get_loan_resp, CommonResponseKeys.STATS).raw}\n")

loan_detail_data = response_args.copy()
loan_detail_data[LoanDetailDataTableKeys.DATA_TABLE] = loan_detail_data_table
loan_detail_resp = GetLoanDetail(**loan_detail_data)
loan_detail_resp.show_data_table()
print(f"RAW STATS DATA: {getattr(loan_detail_resp, CommonResponseKeys.STATS).raw}")
print(f"VERSION: {loan_detail_resp.Version.full_version_info()}\n")
