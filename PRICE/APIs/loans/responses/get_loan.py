from PRICE.APIs.loans.models.add_loan_data import (
    AddLoanDataTable, AddLoanDataTableKeys, AddLoanDataColEntryKeys, AddLoanRowValueKeys, AddLoanRowColKeys)
from PRICE.base.common.response import CommonResponse


class GetLoan(CommonResponse):

    def __init__(self, **kwargs):
        key = AddLoanDataTableKeys.DATA_TABLE
        model = AddLoanDataTable

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        kwargs[key] = model(**kwargs.get(key, {}))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)

    def show_data_table(self):
        table_data = getattr(self, AddLoanDataTableKeys.DATA_TABLE)
        table = [[getattr(col, AddLoanDataColEntryKeys.LABEL) for col in
                  getattr(table_data, AddLoanDataTableKeys.COLS)]]

        for row_dict in getattr(table_data, AddLoanDataTableKeys.ROWS):
            row_data = [getattr(row, AddLoanRowValueKeys.VALUE) for row in getattr(row_dict, AddLoanRowColKeys.COL)]
            table.append(row_data)

        # TODO: Create proper ASCII table via PrettyTable or implement simple array table
        print(table)
