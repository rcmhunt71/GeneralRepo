from PRICE.common.response import CommonResponse
from PRICE.loans.models.loan_status import LoanStatusKeys, LoanStatuses


class GetLoanStatuses(CommonResponse):

    def __init__(self, **kwargs):
        key = LoanStatusKeys.LOAN_STATUSES
        model = LoanStatuses

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)
        kwargs[key] = model(*kwargs.get(key))
        super().__init__(objs=self._OBJS, **kwargs)
