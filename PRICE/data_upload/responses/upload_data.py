from PRICE.common.response import CommonResponse
from PRICE.data_upload.models.upload_data import UploadDataKeys


class UploadData(CommonResponse):
    ADD_KEYS = [UploadDataKeys.TOKEN, UploadDataKeys.VALID_UNTIL]
    SUB_MODELS = [None, None]
