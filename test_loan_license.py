import unittest
from random import choice, randrange

from PRICE.APIs.loans.client import LoanClient
from PRICE.APIs.loans.models.license_data import License, LicenseInfoKeys, Licenses, LicenseDataKeys
from PRICE.APIs.loans.requests.get_loan_license_data import UnknownDataFromTypeException, LoanLicenseDataFrom
from PRICE.APIs.loans.responses.get_loan_license_data import GetLoanLicenseDataResponse
from PRICE.APIs.loans.requests.set_loan_license_data import SetLoanLicenseDataParams

from PRICE.logger.logging import Logger
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

log = Logger()


# ================================================================
#     Client Info
# ================================================================
BASE_URL = "auto.test.pclender.dom"
DATABASE = "testset1"
PORT = 8080

NONCE = "DEADBEEF15DECEA5ED"
SESSION_ID = 1232465798
LOAN_NUMEBER_ID = f"{randrange(999999):06}"

# --------------------------------------------------
#             LOAN LICENSE DATA
# --------------------------------------------------
LOAN_TYPES = ["General", "FHA", "VA"]
NUMBER_OF_LICENSES = 3


def build_date():
    return (f"{randrange(2005, 2019)}-{randrange(1, 12):02}-{randrange(1, 28):02}T"
            f"{randrange(24):02}:{randrange(60):02}:{randrange(60):02}")


def build_license_data():
    return {
        LicenseInfoKeys.LICENSE_ID: randrange(9),
        LicenseInfoKeys.LICENSE_NAME: f"Alaska Exemption Letter #{randrange(99)}:2",
        LicenseInfoKeys.LICENSE_NUMBER: "".join([str(x) for x in [randrange(9) for _ in range(9)]]),
        LicenseInfoKeys.LICENSE_FROM: build_date(),
        LicenseInfoKeys.LICENSE_EXPIRES: build_date(),
        LicenseInfoKeys.STATE: "AK",
        LicenseInfoKeys.STATE_DEFAULT: False,
        LicenseInfoKeys.LIEN_POSITION: 4564,
        LicenseInfoKeys.LICENSE_TYPE: choice(LOAN_TYPES),
        LicenseInfoKeys.DBAID: randrange(9),
    }


licenses_data = [build_license_data() for _ in range(NUMBER_OF_LICENSES)]


# --------------------------------------------------
#             LOAN LICENSE TESTS
# --------------------------------------------------
class TestLoanLicenses(unittest.TestCase, CommonResponseValidations):
    def test_license_model(self):
        index = randrange(NUMBER_OF_LICENSES)
        license_obj = License(**licenses_data[index])
        self._validate_response(model=license_obj, model_data=licenses_data[index])

    def test_licenses_list_model(self):
        licenses_info = Licenses(*licenses_data)
        self._verify(
            descript=f"{licenses_info.model_name} - Number of license objects are equal",
            actual=len(licenses_info), expected=len(licenses_data))

        for index, elem in enumerate(licenses_info):
            self._validate_response(model=elem, model_data=licenses_data[index])

    def test_licenses_response_model(self):
        primary_license_data_key = LicenseDataKeys.LICENSE_DATA

        licenses_args = response_args.copy()
        licenses_args[LicenseDataKeys.LICENSE_DATA] = licenses_data
        get_license_info_resp = GetLoanLicenseDataResponse(**licenses_args)

        self._verify(
            descript=f"{get_license_info_resp.model_name} - has '{primary_license_data_key}' attribute",
            actual=hasattr(get_license_info_resp, primary_license_data_key), expected=True)

        self._verify(
            descript=f"{get_license_info_resp.model_name} - Number of license objects are equal",
            actual=len(getattr(get_license_info_resp, primary_license_data_key)), expected=len(licenses_data))

        data = getattr(get_license_info_resp, primary_license_data_key)
        keys = licenses_data[0].keys()
        for index, model in enumerate(data):
            for attr in keys:
                self._verify(
                    descript=f"{get_license_info_resp.model_name} #{index} - Attribute '{attr}' exists in model",
                    actual=hasattr(model, attr), expected=True)

                self._verify(
                    descript=f"{get_license_info_resp.model_name} #{index} - Attribute '{attr}' value matches data.",
                    actual=getattr(model, attr), expected=licenses_data[index][attr])

        self._validate_response(model=get_license_info_resp, model_data=licenses_args)


class TestLoanLicenseClient(unittest.TestCase, CommonResponseValidations):
    def test_GetLoanLicenseData_client(self):
        licenses_args = response_args.copy()
        licenses_args[LicenseDataKeys.LICENSE_DATA] = licenses_data

        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=licenses_args)

        response_model = client.get_loan_license_data(
            session_id=SESSION_ID, nonce=NONCE,
            loan_number_id=LOAN_NUMEBER_ID, data_from=LoanLicenseDataFrom.LOAN_OFFICER.value,
            data_id=randrange(99999999))

        self._show_response(response_model=response_model)
        self._validate_response(model=response_model, model_data=licenses_args)

    def test_GetLoanLicenseData_client_unknown_data_for_datafrom_type(self):
        licenses_args = response_args.copy()
        licenses_args[LicenseDataKeys.LICENSE_DATA] = licenses_data

        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=licenses_args)

        with self.assertRaises(UnknownDataFromTypeException):
            client.get_loan_license_data(
                session_id=SESSION_ID, nonce=NONCE,
                loan_number_id=LOAN_NUMEBER_ID, data_from=1001, data_id=randrange(99999999))

    def test_SetLoanLicenseData_client(self):
        license_args = response_args.copy()

        params = {
            'data_from': 2,
            'license_id': 887766556,
            'license_name': "TEST_License",
            'license_number': 123456,
            'license_state': "TX",
        }

        client = LoanClient(base_url=BASE_URL, database=DATABASE, port=PORT)
        client.insert_test_response_data(data=license_args)
        response_model = client.set_loan_license_data(
            session_id=SESSION_ID, nonce=NONCE, loan_number_id=LOAN_NUMEBER_ID, **params)
        self._validate_response(model=response_model, model_data=license_args)

        param_str = "&".join([f"{getattr(SetLoanLicenseDataParams, key.upper())}={value}" for key, value
                              in params.items()])
        self.assertIn(param_str, response_model.response.params)


if __name__ == '__main__':
    unittest.main()
