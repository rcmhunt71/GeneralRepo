from dataclasses import dataclass

from PRICE.abstract.base_response import BaseListResponse
from PRICE.company.models.company import Company


@dataclass
class CompaniesKeys:
    COMPANIES: str = 'Companies'


class Companies(BaseListResponse):
    SUB_MODEL = Company
