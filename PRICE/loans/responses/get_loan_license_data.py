from PRICE.common.response import CommonResponse
from PRICE.loans.models.license_data import Licenses, LicenseDataKeys


class GetLoanLicenseData(CommonResponse):
    ADD_KEYS = [LicenseDataKeys.LICENSE_DATA]
    SUB_MODELS = [Licenses]
