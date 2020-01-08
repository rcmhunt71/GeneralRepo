from dataclasses import dataclass


@dataclass
class EmailMergeKeys:
    SUBJECT: str = "Subject"
    BODY: str = "Body"


@dataclass
class EmailConvLogKeys:
    MEMO_ID: str = "MemoID"
