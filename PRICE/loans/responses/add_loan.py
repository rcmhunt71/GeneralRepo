from dataclasses import dataclass

from PRICE.common.response import CommonResponse


@dataclass
class AddLoanKeys:
    NEW_LOAN_NUMBER_ID: str = "NewLoanNumberID"


class AddLoan(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [AddLoanKeys.NEW_LOAN_NUMBER_ID]
        super().__init__(keys=self._VARS, **kwargs)

    def get_loan_id(self):
        return getattr(self, AddLoanKeys.NEW_LOAN_NUMBER_ID, None)
