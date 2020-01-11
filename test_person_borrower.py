from random import choice, randrange
import unittest

from PRICE.APIs.person.borrower.models.borrower import Borrower, BorrowerKeys, BorrowerDetailList, BorrowerDetailKeys
from PRICE.APIs.person.borrower.responses.get_borrower import GetBorrower
from PRICE.APIs.person.borrower.responses.get_customers import GetCustomers
from PRICE.APIs.person.borrower.responses.set_customer import SetCustomer
from PRICE.APIs.person.borrower.models.customers import Customer, CustomerKeys, CustomerList, CustomerListKeys
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

NUMBER_OF_BORROWERS = 7
NUMBER_OF_CUSTOMERS = 5


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


if __name__ == "__main__":
    unittest.main()
