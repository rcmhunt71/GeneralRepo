from PRICE.common.response import CommonResponse
from PRICE.notification.models.email import EmailConvLogKeys


class SendEmailAndMakeConvLog(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [EmailConvLogKeys.MEMO_ID]
        super().__init__(keys=self._VARS, **kwargs)
