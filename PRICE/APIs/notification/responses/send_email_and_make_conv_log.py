from PRICE.APIs.notification.models.email import EmailConvLogKeys
from PRICE.base.common.response import CommonResponse


class SendEmailAndMakeConvLog(CommonResponse):
    ADD_KEYS = [EmailConvLogKeys.MEMO_ID]
    SUB_MODELS = [None]
