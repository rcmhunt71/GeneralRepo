from dataclasses import dataclass
from enum import Enum

from PRICE.base.common.models.request import BaseRequestModel, BaseRequestModelKeys


class UnknownDataFromTypeException(Exception):
    pass


@dataclass
class GetLicenseLoanDataRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    DATA_FROM: str = "DataFrom"
    DATA_ID: str = "DataID"


class LoanLicenseDataFrom(Enum):
    LENDER = 0
    LOAN_OFFICER = 1
    BROKER_COMPANY = 2
    BROKER_PERSON = 3
    BUYER_COMPANY = 4
    BUYER_PERSON = 5
    SELLER_COMPANY = 6
    SELLER_PERSON = 7
    SETTLEMENT_COMPANY = 8
    SETTLEMENT_PERSON = 9


class GetLoanLicenseDataRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id, data_from, data_id):
        self.loan_number_id = loan_number_id
        if isinstance(data_from, Enum):
            self.data_from = data_from.value
        elif isinstance(data_from, int) and data_from in [x.value for x in LoanLicenseDataFrom]:
            self.data_from = data_from
        else:
            raise UnknownDataFromTypeException(f"Unknown LoanLicenseDataRequest data_from entry: {data_from}")

        self.data_id = data_id
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        return {
            GetLicenseLoanDataRequestParams.SESSION_ID: self.session_id,
            GetLicenseLoanDataRequestParams.NONCE: self.nonce,
            GetLicenseLoanDataRequestParams.LOAN_NUMBER_ID: self.loan_number_id,
            GetLicenseLoanDataRequestParams.DATA_FROM: self.data_from,
            GetLicenseLoanDataRequestParams.DATA_ID: self.data_id,
        }
