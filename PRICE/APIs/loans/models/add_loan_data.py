from dataclasses import dataclass

from PRICE.base.abstract.base_response import BaseResponse, BaseListResponse


# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------


@dataclass
class AddLoanDataColEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


class AddLoanDataColEntry(BaseResponse):
    ADD_KEYS = [AddLoanDataColEntryKeys.ID, AddLoanDataColEntryKeys.LABEL,
                AddLoanDataColEntryKeys.TYPE]


class AddLoanDataCols(BaseListResponse):
    SUB_MODEL = AddLoanDataColEntry

# --------------------------------
# ROW DEFINITIONS
# --------------------------------


@dataclass
class AddLoanRowValueKeys:
    VALUE: str = "v"


@dataclass
class AddLoanRowColKeys:
    COL: str = "c"


class AddLoanValueEntry(BaseResponse):
    ADD_KEYS = [AddLoanRowValueKeys.VALUE]
    SUB_MODELS = [None]


class AddLoanRowColsValue(BaseListResponse):
    SUB_MODEL = AddLoanValueEntry


class AddLoanRowEntry(BaseResponse):
    ADD_KEYS = [AddLoanRowColKeys.COL]
    SUB_MODELS = [AddLoanRowColsValue]


class AddLoanRowList(BaseListResponse):
    SUB_MODEL = AddLoanRowEntry

# --------------------------------
# TABLE DEFINITIONS
# --------------------------------


@dataclass
class AddLoanDataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"


class AddLoanDataTable(BaseResponse):
    ADD_KEYS = [AddLoanDataTableKeys.ROWS, AddLoanDataTableKeys.COLS]
    SUB_MODELS = [AddLoanRowList, AddLoanDataCols]

