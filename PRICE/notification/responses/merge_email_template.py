from PRICE.common.response import CommonResponse
from PRICE.notification.models.email import EmailMergeKeys


class MergeEmailTemplate(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [EmailMergeKeys.SUBJECT, EmailMergeKeys.BODY]
        super().__init__(keys=self._VARS, **kwargs)
