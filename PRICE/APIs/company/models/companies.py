from dataclasses import dataclass

from PRICE.APIs.company.models.company import Company
from PRICE.base.abstract.base_response import BaseListResponse


@dataclass
class CompaniesKeys:
    COMPANIES: str = 'Companies'


class Companies(BaseListResponse):
    SUB_MODEL = Company
