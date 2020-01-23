from base.clients.base_client import BaseClient

from APIs.loans.client import LoanClient


class Client(BaseClient):
    def __init__(self, base_url, database, port, headers):
        super().__init__(base_url=base_url, database=database, port=port, headers=headers)
        self.loan = LoanClient(client=self)
