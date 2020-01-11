from random import choice, randrange
import unittest

from PRICE.APIs.person.borrower.models.borrower import Borrower, BorrowerKeys, BorrowerDetailList, BorrowerDetailKeys
from PRICE.APIs.person.borrower.models.loan_list import (
    LoanListHeaderEntryKeys, LoanListHeaderEntry, LoanListHeaderList, LoanListRowValueEntryKeys, LoanListRowValueEntry,
    LoanListRowValuesList, LoanListRowColValueEntryKeys, LoanListRowCol, LoanListRowColList, LoanListRowsKeys,
    LoanListHeaderColumnKeys, CustomerLoanListKeys, CustomerLoanList
)
from PRICE.APIs.person.borrower.responses.get_borrower import GetBorrower
from PRICE.APIs.person.borrower.responses.get_customers import GetCustomers
from PRICE.APIs.person.borrower.responses.get_customer_loan_list import GetCustomerLoanList
from PRICE.APIs.person.borrower.responses.set_customer import SetCustomer
from PRICE.APIs.person.borrower.models.customers import Customer, CustomerKeys, CustomerList, CustomerListKeys
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

NUMBER_OF_BORROWERS = 7
NUMBER_OF_CUSTOMERS = 5
NUMBER_OF_HEADERS = 4
NUMBER_OF_ROWS = 10


def build_borrower():
    return {
        BorrowerKeys.PERSON_ID: randrange(9999),
        BorrowerKeys.FIRST_NAME: choice(["Fred", "John", "Jane", "Jill", "Mortimer", "Frieda"]),
        BorrowerKeys.LAST_NAME: choice(["Jones", "Smith", "McTavish", "Beaumont", "Humphries", "Katovich"]),
    }


def build_customer():
    return {
        CustomerKeys.CUSTOMER_ID: randrange(999999),
        CustomerKeys.DECLARE_A: choice(["A", "B", "C", "D", "E"]),
        CustomerKeys.DECLARE_B: choice(["V", "W", "X", "Y", "Z"]),
    }


def build_loan_list_entry():
    return {
        LoanListHeaderEntryKeys.ID: choice(["Loan_Number", "Borrower_Number", "Customer_ID"]),
        LoanListHeaderEntryKeys.LABEL: choice(["Loan Number", "Borrower Name", "Customer ID"]),
        LoanListHeaderEntryKeys.TYPE: choice(["number", "string", "UUID", "CTYPE"])
    }


def build_loan_list_row_entry():
    return {LoanListRowValueEntryKeys.VALUE: randrange(999999)}


class TestPersonBorrower(unittest.TestCase, CommonResponseValidations):
    def test_borrower_model(self):
        data = build_borrower()
        model = Borrower(**data)
        self._validate_response(model=model, model_data=data)

    def test_borrower_list_model(self):
        data = [build_borrower() for _ in range(NUMBER_OF_BORROWERS)]
        model = BorrowerDetailList(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_GetBorrower_Response(self):
        key = BorrowerDetailKeys.BORROWER_DETAIL

        data = response_args.copy()
        data[key] = [build_borrower() for _ in range(NUMBER_OF_BORROWERS)]
        response = GetBorrower(**data)

        self._verify(f"{response.model_name}: Verify response has '{key}' attribute.",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)


class TestPersonCustomer(unittest.TestCase, CommonResponseValidations):
    def test_customer_model(self):
        data = build_customer()
        model = Customer(**data)
        self._validate_response(model=model, model_data=data)

    def test_customer_list(self):
        data = [build_customer() for _ in range(NUMBER_OF_CUSTOMERS)]
        model = CustomerList(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_GetCustomer_response(self):
        key = CustomerListKeys.CUSTOMERS

        data = response_args.copy()
        data[key] = [build_customer() for _ in range(NUMBER_OF_CUSTOMERS)]
        response = GetCustomers(**data)

        self._verify(f"{response.model_name}: Verify response has '{key}' attribute.",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)

    def test_SetCustomer_response(self):
        key = CustomerListKeys.CUSTOMERS

        data = response_args.copy()
        data[key] = [build_customer() for _ in range(NUMBER_OF_CUSTOMERS)]
        response = SetCustomer(**data)

        self._verify(f"{response.model_name}: Verify response has '{key}' attribute.",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)


class TestCustomerLoanList(unittest.TestCase, CommonResponseValidations):
    def test_loan_list_header_entries_model(self):
        data = build_loan_list_entry()
        model = LoanListHeaderEntry(**data)
        self._validate_response(model=model, model_data=data)

    def test_loan_list_header_list_model(self):
        data = [build_loan_list_entry() for _ in range(NUMBER_OF_HEADERS)]
        model = LoanListHeaderList(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_loan_list_row_value_model(self):
        data = build_loan_list_row_entry()
        model = LoanListRowValueEntry(**data)
        self._validate_response(model=model, model_data=data)

    def test_loan_list_row_list_model(self):
        data = [build_loan_list_row_entry() for _ in range(NUMBER_OF_ROWS)]
        model = LoanListRowValuesList(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_loan_list_rew_col_model(self):
        data = {LoanListRowColValueEntryKeys.COL: [build_loan_list_row_entry() for _ in range(NUMBER_OF_HEADERS)]}
        model = LoanListRowCol(**data)
        self._validate_response(model=model, model_data=data)

    def test_loan_list_row_col_list(self):
        data = [{LoanListRowColValueEntryKeys.COL:
                     [build_loan_list_row_entry() for _ in range(NUMBER_OF_HEADERS)]} for _ in range(NUMBER_OF_ROWS)]
        model = LoanListRowColList(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_customer_loan_list_model(self):
        header_data = [build_loan_list_entry() for _ in range(NUMBER_OF_HEADERS)]
        row_data = [{LoanListRowColValueEntryKeys.COL:
                    [build_loan_list_row_entry() for _ in range(NUMBER_OF_HEADERS)]} for _ in range(NUMBER_OF_ROWS)]

        data = {LoanListHeaderColumnKeys.COLS: header_data,
                LoanListRowsKeys.ROWS: row_data}
        model = CustomerLoanList(**data)
        self._validate_response(model=model, model_data=data)

    def test_CustomerLoanList_response(self):
        header_data = [build_loan_list_entry() for _ in range(NUMBER_OF_HEADERS)]
        row_data = [{LoanListRowColValueEntryKeys.COL:
                    [build_loan_list_row_entry() for _ in range(NUMBER_OF_HEADERS)]} for _ in range(NUMBER_OF_ROWS)]

        args = response_args.copy()
        args[CustomerLoanListKeys.CUSTOMER_LOAN] = {LoanListHeaderColumnKeys.COLS: header_data,
                                                    LoanListRowsKeys.ROWS: row_data}
        response = GetCustomerLoanList(**args)
        self._validate_response(model=response, model_data=args)


if __name__ == "__main__":
    unittest.main()
