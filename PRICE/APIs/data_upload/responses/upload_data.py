from PRICE.APIs.data_upload.models.upload_data import UploadDataKeys
from PRICE.base.common.response import CommonResponse


class UploadData(CommonResponse):
    ADD_KEYS = [UploadDataKeys.TOKEN, UploadDataKeys.VALID_UNTIL]
    SUB_MODELS = [None, None]
