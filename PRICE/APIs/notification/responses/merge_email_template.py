from APIs.notification.models.email import EmailMergeKeys
from base.common.response import CommonResponse


class MergeEmailTemplate(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [EmailMergeKeys.SUBJECT, EmailMergeKeys.BODY]
        super().__init__(keys=self._VARS, **kwargs)
