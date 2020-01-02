from dataclasses import dataclass

from PRICE.company.models.company import Company


@dataclass
class CompaniesKeys:
    COMPANIES: str = 'Companies'


class Companies(list):
    def __init__(self, *args):
        super().__init__()
        self.extend([Company(**company_dict) for company_dict in args])

    def to_struct(self):
        return [x.to_struct() for x in self]
