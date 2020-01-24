from dataclasses import dataclass
from enum import Enum

from base.clients.base_client import BaseClient
from PRICE.base.common.models.request import BaseRequestModel

from PRICE.APIs.loans.responses.add_loan import AddALoanResponse, ImportFromFileResponse, ImportFromFileWithDateResponse
from PRICE.APIs.loans.responses.get_loan import GetLoanResponse
from PRICE.APIs.loans.responses.get_loan_detail import GetLoanDetailResponse
from PRICE.APIs.loans.responses.get_final_value_tags import GetFinalValueTagsResponse
from PRICE.APIs.loans.responses.get_loan_license_data import GetLoanLicenseDataResponse
from PRICE.APIs.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetailsResponse
from PRICE.APIs.loans.responses.get_loan_statuses import GetLoanStatusesResponse
from PRICE.APIs.loans.responses.set_anti_steering_data import SetAntiSteeringDataResponse
from PRICE.APIs.loans.responses.set_loan_data import SetLoanDataResponse
from PRICE.APIs.loans.responses.set_loan_hdma import SetLoanHDMAResponse

from PRICE.APIs.loans.requests.add_loan import ImportFromFileRequest, ImportFromFileWithDateRequest
from PRICE.APIs.loans.requests.get_loan import GetLoanRequest, GetLoanDetailRequest, GetFinalValueTagsRequest
from PRICE.APIs.loans.requests.get_loan_license_data import GetLoanLicenseDataRequest
from PRICE.APIs.loans.requests.get_loan_rate_quote_details import GetLoanRateQuoteDetailsRequest
from PRICE.APIs.loans.requests.get_loan_statuses import GetLoanStatusesRequest
from PRICE.APIs.loans.requests.set_anti_steering_data import SetAntiSteeringDataRequest
from PRICE.APIs.loans.requests.set_loan_data import SetLoanDataRequest
from PRICE.APIs.loans.requests.set_loan_hmda import SetLoanHDMARequest


class ImportFromFileFileTypes(Enum):
    LOSFILE = 0
    FANNIE_MAE = 1
    MISMO_AUS = 2
    IHM = 3
    MISMO_NYLX = 4


@dataclass
class ApiEndpoints:
    ADD_A_LOAN: str = "add_a_loan"
    GET_FINAL_VALUE_TAG: str = "get_final_value_tags"
    GET_LOAN: str = "get_loan"
    GET_LOAN_DETAIL: str = "get_loan_detail"
    GET_LOAN_LICENSE_DATA: str = "get_loan_license_data"
    GET_LOAN_RATE_QUOTE_DETAILS: str = "get_loan_rate_quote_details"
    GET_LOAN_STATUSES: str = "get_loan_statuses"
    IMPORT_FROM_FILE: str = "import_from_file"
    IMPORT_FROM_FILE_WITH_DATE: str = "import_from_file_with_date"
    SET_ANTI_STEERING_DATA: str = "set_anti_steering_data"
    SET_LOAN_DATA: str = "set_loan_data"
    SET_LOAN_HDMA: str = "set_loan_hdma"

class LoanClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"

    def add_loan(self, session_id, nonce):
        request_model = BaseRequestModel(session_id=session_id, nonce=nonce)
        response_model = AddALoanResponse
        endpoint = ApiEndpoints.ADD_A_LOAN
        headers = {}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={}, headers=headers,
                             params=request_model.as_params_dict)
        return response

    def import_from_file(self, session_id, nonce, loan_number, file_type, date_name, base64_file_data):
        request_model = ImportFromFileRequest(session_id=session_id, nonce=nonce, loan_number=loan_number,
                                              file_type=file_type, date_name=date_name,
                                              base64_file_data=base64_file_data)
        response_model = ImportFromFileResponse
        endpoint = ApiEndpoints.IMPORT_FROM_FILE
        headers = {}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={}, headers=headers,
                             params=request_model.as_params_dict, binary_data=base64_file_data)
        return response

    def import_from_file_with_date(self, session_id, nonce, upload_token, file_type, loan_number, b2b_flag, date_name):
        request_model = ImportFromFileWithDateRequest(session_id=session_id, nonce=nonce, loan_number=loan_number,
                                                      file_type=file_type, date_name=date_name, b2b_flag=b2b_flag,
                                                      upload_token=upload_token)
        response_model = ImportFromFileWithDateResponse
        endpoint = ApiEndpoints.IMPORT_FROM_FILE_WITH_DATE
        headers = {}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={}, headers=headers,
                             params=request_model.as_params_dict)
        return response

    def get_loan(self, session_id, nonce, loan_number_id):
        request_model = GetLoanRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetLoanResponse
        endpoint = ApiEndpoints.GET_LOAN
        headers = {}

        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                            params=request_model.as_params_dict)
        return response

    def get_loan_detail(self, session_id, nonce, loan_number_id):
        request_model = GetLoanDetailRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetLoanDetailResponse
        endpoint = ApiEndpoints.GET_LOAN_DETAIL
        headers = {}

        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                            params=request_model.as_params_dict)
        return response

    def get_final_value_tags(self, session_id, nonce, loan_number_id):
        request_model = GetFinalValueTagsRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetFinalValueTagsResponse
        endpoint = ApiEndpoints.GET_FINAL_VALUE_TAG
        headers = {}

        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                            params=request_model.as_params_dict)
        return response

    def get_loan_license_data(self, session_id, nonce, loan_number_id, data_from, data_id):
        request_model = GetLoanLicenseDataRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id,
                                                  data_from=data_from, data_id=data_id)
        response_model = GetLoanLicenseDataResponse
        endpoint = ApiEndpoints.GET_LOAN_LICENSE_DATA
        headers = {}

        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                            params=request_model.as_params_dict)
        return response

    def get_loan_rate_quote_details(self, session_id, nonce, loan_number_id):
        request_model = GetLoanRateQuoteDetailsRequest(session_id=session_id, nonce=nonce,
                                                       loan_number_id=loan_number_id)
        response_model = GetLoanRateQuoteDetailsResponse
        endpoint = ApiEndpoints.GET_LOAN_RATE_QUOTE_DETAILS
        headers = {}

        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                            params=request_model.as_params_dict)
        return response

    def get_loan_statuses(self, session_id, nonce, loan_number_id):
        request_model = GetLoanStatusesRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id)
        response_model = GetLoanStatusesResponse
        endpoint = ApiEndpoints.GET_LOAN_STATUSES
        headers = {}

        response = self.get(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                            params=request_model.as_params_dict)
        return response

    def set_anti_steering_data(self, session_id, nonce, loan_number_id, index=None, program_id=None, rate=None,
                               loan_origination=None, loan_discount=None, sales_price=None, value=None,
                               base_loan_amount=None, other_financing=None, payload_dict=None):

        request_model = SetAntiSteeringDataRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id,
                                                   index=index, program_id=program_id, rate=rate, value=value,
                                                   loan_discount=loan_discount, loan_origination=loan_origination,
                                                   base_loan_amount=base_loan_amount, other_financing=other_financing,
                                                   sales_price=sales_price, payload_dict=payload_dict)
        response_model = SetAntiSteeringDataResponse
        endpoint = ApiEndpoints.SET_ANTI_STEERING_DATA
        headers = {self.CONTENT_TYPE: self.APPLICATION_JSON}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response

    def set_loan_data(self, session_id, nonce, loan_number_id, payload_dict=None, **kwargs):
        # For valid arguments, use lowercase name of attributes listed in API.loans.request.set_loan.SetLoanDataPayload

        request_model = SetLoanDataRequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id,
                                           payload_dict=payload_dict, **kwargs)
        response_model = SetLoanDataResponse
        endpoint = ApiEndpoints.SET_LOAN_DATA
        headers = {self.CONTENT_TYPE: self.APPLICATION_JSON}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response

    def set_loan_hdma(self, session_id, nonce, loan_number_id=None, payload_dict=None, **kwargs):
        # For valid arguments, use lowercase name of attributes listed in API.loans.request.set_loan.SetLoanHDMARequest

        request_model = SetLoanHDMARequest(session_id=session_id, nonce=nonce, loan_number_id=loan_number_id,
                                           payload_dict=payload_dict, **kwargs)
        response_model = SetLoanHDMAResponse
        endpoint = ApiEndpoints.SET_LOAN_DATA
        headers = {self.CONTENT_TYPE: self.APPLICATION_JSON}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, headers=headers,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response
