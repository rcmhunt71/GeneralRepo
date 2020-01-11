from PRICE.APIs.person.borrower.models.borrower import BorrowerDetailKeys, BorrowerDetailList
from PRICE.base.common.response import CommonResponse


class GetBorrower(CommonResponse):
    ADD_KEYS = [BorrowerDetailKeys.BORROWER_DETAIL]
    SUB_MODELS = [BorrowerDetailList]

