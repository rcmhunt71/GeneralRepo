import unittest
from random import choice

from PRICE.company.models.companies import CompaniesKeys, Companies
from PRICE.company.models.company import CompanyKeys, Company
from PRICE.company.responses.add_company import AddCompanyResponse
from PRICE.company.responses.get_companies import GetCompaniesResponse
from PRICE.company.responses.get_company_ids import GetCompanyIDsResponse, GetCompanyIDsKeys
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# ---------------------------------------------------------------
#            COMPANY TEST DATA
# ---------------------------------------------------------------

company_ids_list = [
    123,
    456,
    789,
    98,
    333,
    777
]

company_args_1 = {
    CompanyKeys.COMPANY_ID: choice(company_ids_list),
    CompanyKeys.COMPANY_NAME: 'Test Company 1',
    CompanyKeys.VOICE: '5558004673',
    CompanyKeys.ADDRESS: "123 SomePlace Drive",
    CompanyKeys.CITY: "Albany",
    CompanyKeys.STATE: "NY",
    CompanyKeys.ZIP: 78108,
}

company_args_2 = {
    CompanyKeys.COMPANY_ID: choice(company_ids_list),
    CompanyKeys.COMPANY_NAME: 'Test Company 2',
    CompanyKeys.VOICE: '5558004674',
    CompanyKeys.ADDRESS: "978 SomeWhere Lane",
    CompanyKeys.CITY: "San Diego",
    CompanyKeys.STATE: "CA",
    CompanyKeys.ZIP: 87404,
}

companies_list = [company_args_1, company_args_2]


# ---------------------------------------------------------------
#     TEST COMPANY MODELS AND RESPONSES
# ---------------------------------------------------------------
class TestCompany(unittest.TestCase, CommonResponseValidations):
    def test_company_model(self):
        company_model = Company(**company_args_1)

        # Verify model has correct data
        self._validate_response(model=company_model, model_data=company_args_1)

    def test_companies_model(self):
        companies_model = Companies(*companies_list)

        # Verify model has correct number of elements and corresponding data
        self.assertEqual(len(companies_list), len(companies_model))
        for index, data_model in enumerate(companies_list):
            self._validate_response(model=companies_model[index], model_data=data_model)

    def test_add_company_response(self):
        add_company_args = response_args.copy()
        company_resp = AddCompanyResponse(**add_company_args)

        # Verify model has correct data
        self._validate_response(model=company_resp, model_data=add_company_args)

    def test_get_companies_response(self):
        get_company_args = response_args.copy()
        get_company_args[CompaniesKeys.COMPANIES] = companies_list
        companies_resp = GetCompaniesResponse(**get_company_args)

        # Verify common response has CompaniesKeys.COMPANIES attribute
        self.assertTrue(hasattr(companies_resp, CompaniesKeys.COMPANIES))
        self.assertEqual(len(getattr(companies_resp, CompaniesKeys.COMPANIES)),
                         len(companies_list))

        # Verify CompaniesKeys.COMPANIES attribute contains correct data
        for index, company_model in enumerate(getattr(companies_resp, CompaniesKeys.COMPANIES)):
            self._validate_response(model=company_model, model_data=companies_list[index])

        # Verify common response portion of response has correct data
        self._validate_response(model=companies_resp, model_data=get_company_args)

    def test_get_company_ids_response(self):
        company_ids_args = response_args.copy()
        company_ids_args[GetCompanyIDsKeys.COMPANY_IDS] = company_ids_list
        company_ids_response = GetCompanyIDsResponse(**company_ids_args)

        # Verify CompaniesKeys.COMPANY_IDs attribute contains correct data
        self.assertListEqual(getattr(company_ids_response, GetCompanyIDsKeys.COMPANY_IDS), company_ids_list)

        # Verify common response portion of response has correct data
        self._validate_response(model=company_ids_response, model_data=company_ids_args)


if __name__ == '__main__':
    unittest.main()
