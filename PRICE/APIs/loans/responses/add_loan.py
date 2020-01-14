from dataclasses import dataclass

from PRICE.base.common.response import CommonResponse


@dataclass
class AddALoanKeys:
    NEW_LOAN_NUMBER_ID: str = "NewLoanNumberID"


class AddALoanResponse(CommonResponse):
    ADD_KEYS = [AddALoanKeys.NEW_LOAN_NUMBER_ID]
    SUB_MODELS = [None]

    def get_loan_id(self):
        return getattr(self, AddALoanKeys.NEW_LOAN_NUMBER_ID, None)


class ImportFromFileResponse(AddALoanResponse):
    pass


class ImportFromFileWithDateResponse(AddALoanResponse):
    pass
