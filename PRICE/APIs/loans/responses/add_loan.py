from dataclasses import dataclass

from PRICE.base.common.response import CommonResponse


@dataclass
class AddLoanKeys:
    NEW_LOAN_NUMBER_ID: str = "NewLoanNumberID"


class AddLoan(CommonResponse):
    ADD_KEYS = [AddLoanKeys.NEW_LOAN_NUMBER_ID]
    SUB_MODELS = [None]

    def get_loan_id(self):
        return getattr(self, AddLoanKeys.NEW_LOAN_NUMBER_ID, None)
