from PRICE.common.response import CommonResponse
from PRICE.data_check.models.datacheck import DataChecks, EvaluateDataCheckBundleKeys


class EvaluateDataCheckBundle(CommonResponse):

    def __init__(self, keys=None, objs=None, **kwargs):
        key = EvaluateDataCheckBundleKeys.DATA_CHECKS

        self._OBJS = [key]
        self._combine_args(keys=keys, objs=objs)

        if kwargs.get(key) is not None:
            kwargs[key] = DataChecks(*kwargs.get(key))

        super().__init__(objs=self._OBJS, **kwargs)