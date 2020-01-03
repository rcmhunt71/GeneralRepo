from PRICE.common.response import CommonResponse
from PRICE.loans.models.loan_detail_data import (
    LoanDetailDataTable, LoanDetailDataTableKeys, LoanDetailColEntryKeys, LoanDetailRowValueKeys,
    LoanDetailRowColKeys)


class GetLoanDetail(CommonResponse):

    def __init__(self, **kwargs):
        key = LoanDetailDataTableKeys.DATA_TABLE
        model = LoanDetailDataTable

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        kwargs[key] = model(**kwargs.get(key))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)

    def show_data_table(self):
        table_data = getattr(self, LoanDetailDataTableKeys.DATA_TABLE)
        table = [[getattr(col, LoanDetailColEntryKeys.ID) for col in
                  getattr(table_data, LoanDetailDataTableKeys.COLS)]]

        for row_dict in getattr(table_data, LoanDetailDataTableKeys.ROWS):
            row_data = [getattr(row, LoanDetailRowValueKeys.VALUE) for row in getattr(row_dict, LoanDetailRowColKeys.COL)]
            table.append(row_data)

        # TODO: Create proper ASCII table via PrettyTable or implement simple array table
        print(table)
