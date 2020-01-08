from APIs.loans.models.loan_status import LoanStatusKeys, LoanStatuses
from base.common.response import CommonResponse


class GetLoanStatuses(CommonResponse):

    def __init__(self, **kwargs):
        key = LoanStatusKeys.LOAN_STATUSES
        model = LoanStatuses

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        kwargs[key] = model(*kwargs.get(key))

        super().__init__(objs=self._OBJS, **kwargs)
