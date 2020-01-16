from enum import Enum

from base.clients.base_client import BaseClient
from PRICE.base.common.models.request import BaseRequestModel

from PRICE.APIs.loans.responses.add_loan import AddALoanResponse, ImportFromFileResponse, ImportFromFileWithDateResponse
from PRICE.APIs.loans.responses.get_loan import GetLoanResponse
from PRICE.APIs.loans.responses.get_loan_detail import GetLoanDetailResponse
from PRICE.APIs.loans.responses.get_final_value_tags import GetFinalValueTagsResponse
from PRICE.APIs.loans.responses.get_loan_license_data import GetLoanLicenseDataResponse

from PRICE.APIs.loans.requests.add_loan import ImportFromFileRequest, ImportFromFileWithDateRequest
from PRICE.APIs.loans.requests.get_loan import GetLoanRequest, GetLoanDetailRequest, GetFinalValueTagsRequest
from PRICE.APIs.loans.requests.get_loan_license_data import GetLoanLicenseDataRequest


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
                                              file_type=file_type, date_name=date_name,
                                              base64_file_data=base64_file_data)
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

    def get_loan(self, session_id, nonce, loan_number_id):
        request_model = GetLoanRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetLoanResponse
        endpoint = "get_loan"
        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=None,
                            params=request_model.as_params_dict)
        return response

    def get_loan_detail(self, session_id, nonce, loan_number_id):
        request_model = GetLoanDetailRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetLoanDetailResponse
        endpoint = "get_loan_detail"
        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=None,
                            params=request_model.as_params_dict)
        return response

    def get_final_value_tags(self, session_id, nonce, loan_number_id):
        request_model = GetFinalValueTagsRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetFinalValueTagsResponse
        endpoint = "get_final_value_tags"
        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=None,
                            params=request_model.as_params_dict)
        return response

    def get_loan_license_data(self, session_id, nonce, loan_number_id, data_from, data_id):
        request_model = GetLoanLicenseDataRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id,
                                                  data_from=data_from, data_id=data_id)
        response_model = GetLoanLicenseDataResponse
        endpoint = "get_loan_license_data"
        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=None,
                            params=request_model.as_params_dict)
        return response
