from dataclasses import dataclass
from PRICE.abstract.base_response import BaseResponse, BaseListResponse

# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------

@dataclass
class DataTableColumnEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


class DataColumnEntry(BaseResponse):
    ADD_KEYS = [DataTableColumnEntryKeys.ID, DataTableColumnEntryKeys.LABEL, DataTableColumnEntryKeys.TYPE]


class DataCols(BaseListResponse):
    SUB_MODEL = DataColumnEntry

# --------------------------------
# ROW DEFINITIONS
# --------------------------------


@dataclass
class DataRowValueKeys:
    VALUE: str = "v"


@dataclass
class DataRowColKeys:
    COL: str = "c"


class RowValueEntry(BaseResponse):
    def __init__(self, **kwargs):
        self._VARS = [DataRowValueKeys.VALUE]
        super().__init__(keys=self._VARS, **kwargs)


class RowColsValue(BaseListResponse):
    SUB_MODEL = RowValueEntry


class RowEntry(BaseResponse):
    ADD_KEYS = [DataRowColKeys.COL]
    SUB_MODELS = [RowColsValue]


class RowList(BaseListResponse):
    SUB_MODEL = RowEntry

# --------------------------------
# TABLE DEFINITIONS
# --------------------------------


@dataclass
class DataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"


class DataTable(BaseResponse):
    ADD_KEYS = [DataTableKeys.ROWS, DataTableKeys.COLS]
    SUB_MODELS = [RowList, DataCols]

