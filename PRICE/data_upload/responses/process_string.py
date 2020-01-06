from PRICE.common.response import CommonResponse
from PRICE.data_upload.models.process_string import ProcessStringKeys


class ProcessString(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [ProcessStringKeys.DL_RESULT, ProcessStringKeys.LOAN_NUMBER_ID, ProcessStringKeys.DATA_LANGUAGE]
        super().__init__(keys=self._VARS, **kwargs)
