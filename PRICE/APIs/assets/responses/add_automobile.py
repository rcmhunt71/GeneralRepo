from APIs.assets.models.automobile import AutomobileKeys
from base.common.response import CommonResponse


class AddAutomobileResponse(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [AutomobileKeys.AUTOMOBILE_ID]
        self._combine_args(keys=self._VARS)

        super().__init__(keys=self._VARS, **kwargs)

