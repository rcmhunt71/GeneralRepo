from dataclasses import dataclass

from PRICE.abstract.base_response import BaseResponse


@dataclass
class CompanyKeys:
    COMPANY_ID: str = "CompanyID"
    COMPANY_NAME: str = "CompanyName"
    VOICE: str = "Voice"
    ADDRESS: str = "Address"
    CITY: str = "City"
    STATE: str = "State"
    ZIP: str = "Zip"


class Company(BaseResponse):
    def __init__(self, **kwargs):
        self._VARS = [CompanyKeys.COMPANY_ID, CompanyKeys.COMPANY_NAME, CompanyKeys.VOICE, CompanyKeys.ADDRESS,
                      CompanyKeys.CITY, CompanyKeys.STATE, CompanyKeys.ZIP, ]
        super().__init__(keys=self._VARS, **kwargs)
