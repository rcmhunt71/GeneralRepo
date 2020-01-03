from dataclasses import dataclass

from PRICE.common.response import CommonResponse
from PRICE.loans.models.loan_data import (DataTable, DataTableKeys, DataTableColumnEntryKeys,
                                          DataRowValueKeys, DataRowColKeys)


@dataclass
class AddLoanKeys:
    NEW_LOAN_NUMBER_ID: str = "NewLoanNumberID"


class AddLoan(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [AddLoanKeys.NEW_LOAN_NUMBER_ID]
        super().__init__(keys=self._VARS, **kwargs)

    def get_loan_id(self):
        return getattr(self, AddLoanKeys.NEW_LOAN_NUMBER_ID, None)


class GetLoan(CommonResponse):
    def __init__(self, **kwargs):
        self._OBJS = [DataTableKeys.DATA_TABLE]
        self._combine_args(objs=self._OBJS)

        kwargs[DataTableKeys.DATA_TABLE] = DataTable(**kwargs.get(DataTableKeys.DATA_TABLE))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)

    def show_data_table(self):
        table_data = getattr(self, DataTableKeys.DATA_TABLE)
        table = [[getattr(col, DataTableColumnEntryKeys.LABEL) for col in
                  getattr(table_data, DataTableKeys.COLS)]]

        for row_dict in getattr(table_data, DataTableKeys.ROWS):
            row_data = [getattr(row, DataRowValueKeys.VALUE) for row in getattr(row_dict, DataRowColKeys.COL)]
            table.append(row_data)

        print(table)
