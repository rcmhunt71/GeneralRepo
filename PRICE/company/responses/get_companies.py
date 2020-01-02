from PRICE.company.models.companies import CompaniesKeys, Companies
from PRICE.common.response import CommonResponse


class GetCompaniesResponse(CommonResponse):

    def __init__(self, keys=None, objs=None, **kwargs):

        self._OBJS = [CompaniesKeys.COMPANIES]
        self._combine_args(keys=keys, objs=objs)

        if kwargs.get(CompaniesKeys.COMPANIES) is not None:
            kwargs[CompaniesKeys.COMPANIES] = Companies(*kwargs.get(CompaniesKeys.COMPANIES))

        super().__init__(objs=self._OBJS, **kwargs)

