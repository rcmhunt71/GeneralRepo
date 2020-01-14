from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse, BaseListResponse


# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------

@dataclass
class LoanDetailColEntryKeys:
    ID: str = "id"
    TYPE: str = "type"


class LoanDetailColEntry(BaseResponse):
    ADD_KEYS = [LoanDetailColEntryKeys.ID, LoanDetailColEntryKeys.TYPE]


class LoanDetailCols(BaseListResponse):
    SUB_MODEL = LoanDetailColEntry


# --------------------------------
# ROW DEFINITIONS
# --------------------------------


@dataclass
class LoanDetailRowValueKeys:
    VALUE: str = "v"


@dataclass
class LoanDetailRowColKeys:
    COL: str = "c"


class LoanDetailRowValueEntry(BaseResponse):
    ADD_KEYS = [LoanDetailRowValueKeys.VALUE]
    SUB_MODELS = [None]


class LoanDetailRowColsValue(BaseListResponse):
    SUB_MODEL = LoanDetailRowValueEntry


class LoanDetailRowEntry(BaseResponse):
    ADD_KEYS = [LoanDetailRowColKeys.COL]
    SUB_MODELS = [LoanDetailRowColsValue]


class LoanDetailRowList(BaseListResponse):
    SUB_MODEL = LoanDetailRowEntry

# --------------------------------
# TABLE DEFINITIONS
# --------------------------------


@dataclass
class LoanDetailDataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"


class LoanDetailDataTable(BaseResponse):
    ADD_KEYS = [LoanDetailDataTableKeys.ROWS, LoanDetailDataTableKeys.COLS]
    SUB_MODELS = [LoanDetailRowList, LoanDetailCols]

