from dataclasses import dataclass

from PRICE.base.common.response import CommonResponse


@dataclass
class GetCompanyIDsKeys:
    COMPANY_IDS: str = 'CompanyIds'


class GetCompanyIDsResponse(CommonResponse):
    ADD_KEYS = [GetCompanyIDsKeys.COMPANY_IDS]
    SUB_MODELS = [None]
