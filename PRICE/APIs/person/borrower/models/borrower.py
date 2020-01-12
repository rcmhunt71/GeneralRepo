from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseListResponse, BaseResponse

@dataclass
class BorrowerKeys:
    PERSON_ID: str = "PersonID"
    LAST_NAME: str = "LastName"
    FIRST_NAME: str = "FirstName"


@dataclass
class BorrowerDetailKeys:
    BORROWER_DETAIL: str = "BorrowerDetail"


class Borrower(BaseResponse):
    ADD_KEYS = [BorrowerKeys.PERSON_ID, BorrowerKeys.LAST_NAME, BorrowerKeys.FIRST_NAME]
    SUB_MODELS = [None for _ in range(len(ADD_KEYS))]


class BorrowerDetailList(BaseListResponse):
    SUB_MODEL = Borrower
