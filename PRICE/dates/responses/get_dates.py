from PRICE.common.response import CommonResponse
from PRICE.dates.models.dates import DatesList, DatesListKeys


class GetDates(CommonResponse):
    def __init__(self, keys=None, objs=None, **kwargs):

        self._OBJS = [DatesListKeys.DATES_LIST]
        self._combine_args(keys=keys, objs=objs)

        if kwargs.get(DatesListKeys.DATES_LIST) is not None:
            kwargs[DatesListKeys.DATES_LIST] = DatesList(*kwargs.get(DatesListKeys.DATES_LIST))

        super().__init__(objs=self._OBJS, **kwargs)
