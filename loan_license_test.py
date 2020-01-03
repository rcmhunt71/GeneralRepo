from PRICE.common.models.stats import StatsKeys
from PRICE.common.models.version import VersionKeys
from PRICE.common.response import CommonResponseKeys
from PRICE.loans.models.license_data import License, LicenseInfoKeys, Licenses, LicenseDataKeys
from PRICE.loans.responses.get_loan_license_data import GetLoanLicenseData

version_args = {
    VersionKeys.MAJOR_VERSION: 10,
    VersionKeys.MINOR_VERSION: 20,
    VersionKeys.BUILD: 30,
    VersionKeys.HOT_FIX: 40,
}

stats_args = {
    StatsKeys.TOTAL_DATABASE_TIME: 35,
    StatsKeys.TOTAL_SERVER_TIME: 25,
    StatsKeys.METHOD_TIME: 15,
    StatsKeys.LOSTIME: 5,
}

response_args = {
    CommonResponseKeys.SUCCESSFUL: True,
    CommonResponseKeys.ERROR_MESSAGE: "Ok",
    CommonResponseKeys.ERROR_CODE: 0,
    CommonResponseKeys.TAGS: "",
    CommonResponseKeys.VERSION: version_args,
    CommonResponseKeys.STATS: stats_args,
    CommonResponseKeys.NONCE: "DEADBEEF-01234",
    CommonResponseKeys.RESPONDER: "E406F3C0BA2DDE5348F99BC0089-1224",
}

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

license_obj = License(**license_data_args_1)
print(f"LicenseData Obj:\n{license_obj}")
print(f"LICENSE ID: {license_obj.LicenseID}")

licenses_info = Licenses(*licenses)
print(f"Second License License Name: '{licenses_info[1].LicenseName}'")

licenses_args = response_args.copy()
licenses_args[LicenseDataKeys.LICENSE_DATA] = licenses
get_license_info_resp = GetLoanLicenseData(**licenses_args)
print(f"First LIC INFO Lien Position: '{get_license_info_resp.Data[0].LienPosition}'")
