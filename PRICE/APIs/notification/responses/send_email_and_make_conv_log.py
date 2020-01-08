from APIs.notification.models.email import EmailConvLogKeys
from base.common.response import CommonResponse


class SendEmailAndMakeConvLog(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [EmailConvLogKeys.MEMO_ID]
        super().__init__(keys=self._VARS, **kwargs)
