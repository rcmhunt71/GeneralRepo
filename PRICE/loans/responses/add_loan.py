from dataclasses import dataclass

from PRICE.common.response import CommonResponse
from PRICE.loans.models.loan_data import DataTable, DataTableKeys

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
