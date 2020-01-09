from PRICE.APIs.loans.models.license_data import Licenses, LicenseDataKeys
from PRICE.base.common.response import CommonResponse


class GetLoanLicenseData(CommonResponse):
    ADD_KEYS = [LicenseDataKeys.LICENSE_DATA]
    SUB_MODELS = [Licenses]
