from PRICE.common.response import CommonResponse
from PRICE.assets.models.automobile import AutomobileKeys


class AddAutomobileResponse(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [AutomobileKeys.AUTOMOBILE_ID]
        self._combine_args(keys=self._VARS)

        super().__init__(keys=self._VARS, **kwargs)

