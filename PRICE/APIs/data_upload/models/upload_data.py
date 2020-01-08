from dataclasses import dataclass


@dataclass
class UploadDataKeys:
    TOKEN: str = "TOKEN"
    VALID_UNTIL: str = "ValidUntil"
