from PRICE.APIs.person.borrower.models.customers import CustomerList, CustomerListKeys
from PRICE.base.common.response import CommonResponse


class SetCustomer(CommonResponse):
    ADD_KEYS = [CustomerListKeys.CUSTOMERS]
    SUB_MODELS = [CustomerList]
