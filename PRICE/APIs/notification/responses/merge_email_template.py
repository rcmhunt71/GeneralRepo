from PRICE.APIs.notification.models.email import EmailMergeKeys
from PRICE.base.common.response import CommonResponse


class MergeEmailTemplate(CommonResponse):
    ADD_KEYS = [EmailMergeKeys.SUBJECT, EmailMergeKeys.BODY]
    SUB_MODELS = [None, None]
