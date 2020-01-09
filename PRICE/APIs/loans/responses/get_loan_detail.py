from PRICE.APIs.loans.models.loan_detail_data import (
    LoanDetailDataTable, LoanDetailDataTableKeys, LoanDetailColEntryKeys, LoanDetailRowValueKeys,
    LoanDetailRowColKeys)
from PRICE.base.common.response import CommonResponse


class GetLoanDetail(CommonResponse):
    ADD_KEYS = [LoanDetailDataTableKeys.DATA_TABLE]
    SUB_MODELS = [LoanDetailDataTable]

    def show_data_table(self):
        table_data = getattr(self, LoanDetailDataTableKeys.DATA_TABLE)
        table = [[getattr(col, LoanDetailColEntryKeys.ID) for col in
                  getattr(table_data, LoanDetailDataTableKeys.COLS)]]

        for row_dict in getattr(table_data, LoanDetailDataTableKeys.ROWS):
            row_data = [getattr(row, LoanDetailRowValueKeys.VALUE) for row in
                        getattr(row_dict, LoanDetailRowColKeys.COL)]
            table.append(row_data)

        # TODO: Create proper ASCII table via PrettyTable or implement simple array table
        print(table)
