from dataclasses import dataclass

from PRICE.base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class GetLoanRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class GetLoanRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        return {
            GetLoanRequestParams.SESSION_ID: self.session_id,
            GetLoanRequestParams.NONCE: self.nonce,
            GetLoanRequestParams.LOAN_NUMBER_ID: self.loan_number_id,
        }
