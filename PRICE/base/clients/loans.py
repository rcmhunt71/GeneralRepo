from PRICE.base.abstract.base_client import BaseClient
from PRICE.base.common.models.request import BaseRequestModel
from PRICE.APIs.loans.responses.add_loan import AddLoan


class LoanClient(BaseClient):

    def add_loan(self, session_id, nonce):
        request_model = BaseRequestModel(session_id=session_id, nonce=nonce)
        response_model = AddLoan
        endpoint = "add_a_loan"

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={},
                             params=request_model.as_params_dict)
        return response
