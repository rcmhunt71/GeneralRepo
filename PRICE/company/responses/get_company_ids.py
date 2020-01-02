from dataclasses import dataclass

from PRICE.common.response import CommonResponse


@dataclass
class GetCompanyIDsKeys:
    COMPANY_IDS: str = 'CompanyIds'


class GetCompanyIDsResponse(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [GetCompanyIDsKeys.COMPANY_IDS]
        print(f"TEST: {self._VARS}")
        super().__init__(keys=self._VARS, **kwargs)
