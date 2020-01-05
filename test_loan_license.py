import unittest

from PRICE.loans.models.license_data import License, LicenseInfoKeys, Licenses, LicenseDataKeys
from PRICE.loans.responses.get_loan_license_data import GetLoanLicenseData
from PRICE.logger.logging import Logger
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

log = Logger()

# --------------------------------------------------
#             LOAN LICENSE DATA
# --------------------------------------------------
license_data_args_1 = {
    LicenseInfoKeys.LICENSE_ID: 8,
    LicenseInfoKeys.LICENSE_NAME: "Alaska Exemption Letter",
    LicenseInfoKeys.LICENSE_NUMBER: "789654125",
    LicenseInfoKeys.LICENSE_FROM: "2017-09-29T00:00:00",
    LicenseInfoKeys.LICENSE_EXPIRES: "2017-05-22T00:00:00.000",
    LicenseInfoKeys.STATE: "AK",
    LicenseInfoKeys.STATE_DEFAULT: False,
    LicenseInfoKeys.LIEN_POSITION: 4564,
    LicenseInfoKeys.LICENSE_TYPE: "General, FHA, VA",
    LicenseInfoKeys.DBAID: 0,
}

license_data_args_2 = {
    LicenseInfoKeys.LICENSE_ID: 9,
    LicenseInfoKeys.LICENSE_NAME: "Alaska Exemption Letter #2",
    LicenseInfoKeys.LICENSE_NUMBER: "78965412533",
    LicenseInfoKeys.LICENSE_FROM: "2017-12-24T00:00:00",
    LicenseInfoKeys.LICENSE_EXPIRES: "2017-12-29T00:00:00.000",
    LicenseInfoKeys.STATE: "AK",
    LicenseInfoKeys.STATE_DEFAULT: False,
    LicenseInfoKeys.LIEN_POSITION: 456423,
    LicenseInfoKeys.LICENSE_TYPE: "General, FHA, VA",
    LicenseInfoKeys.DBAID: 1,
}

licenses = [license_data_args_1, license_data_args_2]


# --------------------------------------------------
#             LOAN LICENSE TESTS
# --------------------------------------------------
class TestLoanLicenses(unittest.TestCase, CommonResponseValidations):
    def test_license_model(self):
        license_obj = License(**license_data_args_1)
        self._validate_response(model=license_obj, model_data=license_data_args_1)

    def test_licenses_list_model(self):
        licenses_info = Licenses(*licenses)
        self._verify(
            descript=f"{licenses_info.model_name} - Number of license objects are equal",
            actual=len(licenses_info), expected=len(licenses))

        for index, elem in enumerate(licenses_info):
            self._validate_response(model=elem, model_data=licenses[index])

    def test_licenses_response_model(self):
        primary_license_data_key = LicenseDataKeys.LICENSE_DATA

        licenses_args = response_args.copy()
        licenses_args[LicenseDataKeys.LICENSE_DATA] = licenses
        get_license_info_resp = GetLoanLicenseData(**licenses_args)

        self._verify(
            descript=f"{get_license_info_resp.model_name} - has '{primary_license_data_key}' attribute",
            actual=hasattr(get_license_info_resp, primary_license_data_key), expected=True)

        self._verify(
            descript=f"{get_license_info_resp.model_name} - Number of license objects are equal",
            actual=len(getattr(get_license_info_resp, primary_license_data_key)), expected=len(licenses))

        data = getattr(get_license_info_resp, primary_license_data_key)
        keys = license_data_args_1.keys()
        for elem in range(len(licenses)):
            for key in keys:
                self.assertEqual(getattr(data[elem], key), licenses[elem][key])

        self._validate_response(model=get_license_info_resp, model_data=licenses_args)


if __name__ == '__main__':
    unittest.main()
