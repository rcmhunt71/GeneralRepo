from dataclasses import dataclass

from PRICE.base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class BaseImportParamKeys(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    FILE_TYPE: str = "FileType"
    DATE_NAME: str = "DateName"


@dataclass
class ImportFromFileParamKeys(BaseImportParamKeys):
    BASE64_FILE_DATA: str = "Base64FileData"


@dataclass
class ImportFromFileWithDataParamKeys(BaseImportParamKeys):
    UPLOAD_TOKEN: str = "UploadToken"
    B2B_FLAG: str = "B2BFlag"


class ImportFromFileRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number, file_type, date_name, base64_file_data):
        self.loan_number = loan_number
        self.file_type = file_type
        self.date_name = date_name
        self.base64_file_data = base64_file_data
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        return {
            ImportFromFileParamKeys.SESSION_ID: self.session_id,
            ImportFromFileParamKeys.NONCE: self.nonce,
            ImportFromFileParamKeys.FILE_TYPE: self.file_type.value,
            ImportFromFileParamKeys.LOAN_NUMBER: self.loan_number,
            ImportFromFileParamKeys.DATE_NAME: self.date_name,
        }


class ImportFromFileWithDateRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number, upload_token, file_type, date_name, b2b_flag):
        self.loan_number = loan_number
        self.upload_token = upload_token
        self.file_type = file_type
        self.date_name = date_name
        self.b2b_flag = b2b_flag
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        return {
            ImportFromFileWithDataParamKeys.SESSION_ID: self.session_id,
            ImportFromFileWithDataParamKeys.NONCE: self.nonce,
            ImportFromFileWithDataParamKeys.FILE_TYPE: self.file_type.value,
            ImportFromFileWithDataParamKeys.LOAN_NUMBER: self.loan_number,
            ImportFromFileWithDataParamKeys.DATE_NAME: self.date_name,
            ImportFromFileWithDataParamKeys.UPLOAD_TOKEN: self.upload_token,
            ImportFromFileWithDataParamKeys.B2B_FLAG: int(self.b2b_flag),
        }

