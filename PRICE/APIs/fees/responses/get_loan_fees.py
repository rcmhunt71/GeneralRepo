from PRICE.base.common.response import CommonResponse
from PRICE.APIs.fees.models.loan_fees import LoanFees, LoanFeeKeys


class GetLoanFees(CommonResponse):
    def __init__(self, keys=None, objs=None, **kwargs):

        key = LoanFeeKeys.LOAN_FEES

        self._OBJS = objs or []
        self._OBJS.append(key)

        if key in kwargs:
            kwargs[key] = LoanFees(**kwargs.get(key, {}))

        super().__init__(keys=keys, objs=self._OBJS, **kwargs)
