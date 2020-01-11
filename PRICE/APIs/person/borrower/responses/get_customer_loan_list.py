from PRICE.base.common.response import CommonResponse

from PRICE.APIs.person.borrower.models.loan_list import CustomerLoanList, CustomerLoanListKeys


class GetCustomerLoanList(CommonResponse):
    ADD_KEYS = [CustomerLoanListKeys.CUSTOMER_LOAN]
    SUB_MODELS = [CustomerLoanList]
