from dataclasses import dataclass

from PRICE.base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class ImportFromFileParamKeys(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    FILE_TYPE: str = "FileType"
    DATE_NAME: str = "DateName"
    BASE64_FILE_DATA: str = "Base64FileData"


class ImportFromFile(BaseRequestModel):
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
