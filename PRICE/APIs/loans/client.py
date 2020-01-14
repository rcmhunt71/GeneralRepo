from enum import Enum

from base.clients.base_client import BaseClient
from PRICE.base.common.models.request import BaseRequestModel
from PRICE.APIs.loans.responses.add_loan import AddALoanResponse, ImportFromFileResponse, ImportFromFileWithDateResponse
from PRICE.APIs.loans.requests.add_loan import ImportFromFileRequest, ImportFromFileWithDateRequest


class ImportFromFileFileTypes(Enum):
    LOSFILE = 0
    FANNIE_MAE = 1
    MISMO_AUS = 2
    IHM = 3
    MISMO_NYLX = 4


class LoanClient(BaseClient):

    def add_loan(self, session_id, nonce):
        request_model = BaseRequestModel(session_id=session_id, nonce=nonce)
        response_model = AddALoanResponse
        endpoint = "add_a_loan"

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={},
                             params=request_model.as_params_dict)
        return response

    def import_from_file(self, session_id, nonce, loan_number, file_type, date_name, base64_file_data):
        request_model = ImportFromFileRequest(session_id=session_id, nonce=nonce, loan_number=loan_number,
                                              file_type=file_type, date_name=date_name, base64_file_data=base64_file_data)
        response_model = ImportFromFileResponse
        endpoint = "import_from_file"

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={},
                             params=request_model.as_params_dict, binary_data=base64_file_data)
        return response

    def import_from_file_with_date(self, session_id, nonce, upload_token, file_type, loan_number, b2b_flag, date_name):
        request_model = ImportFromFileWithDateRequest(session_id=session_id, nonce=nonce, loan_number=loan_number,
                                                      file_type=file_type, date_name=date_name, b2b_flag=b2b_flag,
                                                      upload_token=upload_token)
        response_model = ImportFromFileWithDateResponse
        endpoint = "import_from_file_with_date"

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={},
                             params=request_model.as_params_dict)
        return response
