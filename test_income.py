from random import choice, randrange
import unittest

from PRICE.APIs.income.models.income import IncomeEntryKeys, IncomeEntry, IncomeKeys, IncomeEntries, AddIncomeKeys
from PRICE.APIs.income.responses.add_income import AddIncome
from PRICE.APIs.income.responses.get_incomes import GetIncomes
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

job_positions = ['engineer', 'cashier', 'public servant', 'politician', 'teacher', 'spouse']
other_descriptions = ['Alimony', 'Investments', 'Retired', "None"]

NUMBER_OF_INCOME_SOURCES = 5


def build_income_entry():
    return {
        IncomeEntryKeys.CUSTOMER_ID: randrange(999999999),
        IncomeEntryKeys.INCOME_ID: randrange(10),
        IncomeEntryKeys.COMPANY_ID: randrange(99999999),
        IncomeEntryKeys.INCOME_TYPE: randrange(10),
        IncomeEntryKeys.TITLE_POSITION: choice(job_positions),
        IncomeEntryKeys.BASE_INCOME: randrange(10000, 500000),

        IncomeEntryKeys.OVERTIME: randrange(1000, 10000),
        IncomeEntryKeys.BONUSES: randrange(1000, 10000),
        IncomeEntryKeys.COMMISSION: randrange(1000, 10000),
        IncomeEntryKeys.OTHER: randrange(1000, 10000),

        IncomeEntryKeys.OTHER_DESCRIPTION: choice(other_descriptions),
        IncomeEntryKeys.TOTAL: randrange(5000, 100000),
        IncomeEntryKeys.START_DATE: f"{randrange(2010, 2019)}-{randrange(1, 12)}-{randrange(1, 28)}",
        IncomeEntryKeys.END_DATE: f"{randrange(2010, 2019)}-{randrange(1, 12)}-{randrange(1, 28)}",
        IncomeEntryKeys.YEARS_AT_JOB: randrange(9),
    }


incomes = [build_income_entry() for _ in range(NUMBER_OF_INCOME_SOURCES)]


class TestIncome(unittest.TestCase, CommonResponseValidations):
    def test_income_entry(self):
        data = build_income_entry()
        model = IncomeEntry(**data)
        self._validate_response(model=model, model_data=data)

    def test_incomes_list_model(self):
        model = IncomeEntries(*incomes)

        self._verify(descript=f"{model.model_name} has correct number of elements.",
                     actual=len(model), expected=len(incomes))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=incomes[index])

    def test_GetIncomes_response(self):
        data = response_args.copy()
        data[IncomeKeys.INCOMES] = incomes
        model = GetIncomes(**data)

        key = IncomeKeys.INCOMES
        self._verify(descript=f"{model.model_name} has the {key} attribute",
                     actual=hasattr(model, key), expected=True)
        self._validate_response(model=model, model_data=data)


class TestAddIncome(unittest.TestCase, CommonResponseValidations):
    def test_AddIncome_response(self):
        add_income_args = response_args.copy()
        add_income_args[AddIncomeKeys.INCOME_ID] = randrange(99999999)
        response = AddIncome(**add_income_args)

        self._validate_response(model=response, model_data=add_income_args)


if __name__ == '__main__':
    unittest.main()
