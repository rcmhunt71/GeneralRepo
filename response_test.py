#!/usr/bin/env python

from APIs.configuration.configuration_list import ConfigurationList, ConfigurationListKeys
from APIs.loans.models.loan_detail_data import (
    LoanDetailColEntryKeys, LoanDetailRowValueKeys, LoanDetailDataTableKeys, LoanDetailRowColKeys)
from APIs.loans.responses.get_loan_detail import GetLoanDetailResponse
from PRICE.tests.common_response_args import response_args
from base.common.response import CommonResponseKeys

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

loan_detail_data = response_args.copy()
loan_detail_data[LoanDetailDataTableKeys.DATA_TABLE] = loan_detail_data_table
loan_detail_resp = GetLoanDetailResponse(**loan_detail_data)
loan_detail_resp.show_data_table()
print(f"RAW STATS DATA: {getattr(loan_detail_resp, CommonResponseKeys.STATS).raw}")
print(f"VERSION: {loan_detail_resp.Version.full_version_info()}\n")
