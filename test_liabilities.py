from random import choice, randrange
import unittest

from PRICE.APIs.liability.models.liability import (LiabilitiesKeys, LiabilityEntryKeys, LiabilityEntry,
                                                   LiabilityEntriesList, AddLiabilityKeys)
from PRICE.APIs.liability.responses.get_liabilities import GetLiabilities
from PRICE.APIs.liability.responses.add_liability import AddLiability
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

liability_types = ["other", "revolving", "HELOC", "auto"]
applicant_names = ["Jane Doe", "John Doe", "Freddy Kruger", "Jason (NLN)", "Michael Myers"]
yes_no = ["Yes", "No"]

NUMBER_OF_LIABILITIES = 15


def build_liability_entry():
    return {
        LiabilityEntryKeys.LIABILITY_ID: randrange(10),
        LiabilityEntryKeys.CUSTOMER_ID: randrange(99999999),
        LiabilityEntryKeys.INSTITUTION_ID: randrange(99999999),
        LiabilityEntryKeys.LIABILITY_TYPE: choice(liability_types),
        LiabilityEntryKeys.ACCOUNT_NAME: choice(applicant_names),
        LiabilityEntryKeys.ACCOUNT_NUMBER: randrange(99999999),
        LiabilityEntryKeys.BALANCE: randrange(100000),
        LiabilityEntryKeys.TERM: randrange(60),
        LiabilityEntryKeys.PAYMENT: randrange(10, 1000),
        LiabilityEntryKeys.PAYOFF: randrange(100000),
        LiabilityEntryKeys.TO_BE_PAID_OFF: choice(yes_no)
    }


def build_liabilities_data():
    return [build_liability_entry() for _ in range(NUMBER_OF_LIABILITIES)]


class TestLiabilities(unittest.TestCase, CommonResponseValidations):
    def test_liability_entry_model(self):
        data = build_liability_entry()
        model = LiabilityEntry(**data)
        self._validate_response(model=model, model_data=data)

    def test_liabilities_entries_list_model(self):
        data = build_liabilities_data()
        model = LiabilityEntriesList(*data)

        self._verify(descript=f"{model.model_name} has the correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_GetLiabilities_response(self):
        key = LiabilitiesKeys.LIABILITIES
        data = response_args.copy()
        data[key] = build_liabilities_data()
        response = GetLiabilities(**data)

        self._verify(descript=f"{response.model_name} has {key} attribute",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)


class TestAddLiability(unittest.TestCase, CommonResponseValidations):
    def test_AddLiability_response(self):
        data = response_args.copy()
        data[AddLiabilityKeys.LIABILITY_ID] = randrange(999999)
        response = AddLiability(**data)
        self._validate_response(model=response, model_data=data)


if __name__ == '__main__':
    unittest.main()
