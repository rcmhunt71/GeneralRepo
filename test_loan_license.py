import unittest
from random import choice, randrange

from PRICE.loans.models.license_data import License, LicenseInfoKeys, Licenses, LicenseDataKeys
from PRICE.loans.responses.get_loan_license_data import GetLoanLicenseData
from PRICE.logger.logging import Logger
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

log = Logger()


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
        get_license_info_resp = GetLoanLicenseData(**licenses_args)

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


if __name__ == '__main__':
    unittest.main()
