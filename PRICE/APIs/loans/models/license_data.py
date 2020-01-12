from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class LicenseInfoKeys:
    LICENSE_ID: str = "LicenseID"
    LICENSE_NAME: str = "LicenseName"
    LICENSE_NUMBER: str = "LicenseNumber"
    LICENSE_FROM: str = "LicenseFrom"
    LICENSE_EXPIRES: str = "LicenseExpires"
    STATE: str = "State"
    STATE_DEFAULT: str = "StateDefault"
    LIEN_POSITION: str = "LienPosition"
    LICENSE_TYPE: str = "License Type"
    DBAID: str = "DBAID"


@dataclass
class LicenseDataKeys:
    LICENSE_DATA: str = "Data"


class License(BaseResponse):
    ADD_KEYS = [LicenseInfoKeys.LICENSE_ID, LicenseInfoKeys.LICENSE_NAME, LicenseInfoKeys.LICENSE_NUMBER,
                LicenseInfoKeys.LICENSE_FROM, LicenseInfoKeys.LICENSE_EXPIRES, LicenseInfoKeys.STATE,
                LicenseInfoKeys.STATE_DEFAULT, LicenseInfoKeys.LIEN_POSITION, LicenseInfoKeys.LICENSE_TYPE,
                LicenseInfoKeys.DBAID]
    SUB_MODELS = [None for _ in range(len(ADD_KEYS))]


class Licenses(BaseListResponse):
    SUB_MODEL = License

