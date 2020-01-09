from PRICE.APIs.company.models.companies import CompaniesKeys, Companies
from PRICE.base.common.response import CommonResponse


class GetCompaniesResponse(CommonResponse):
    ADD_KEYS = [CompaniesKeys.COMPANIES]
    SUB_MODELS = [Companies]
