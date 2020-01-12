from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse, BaseListResponse


# COLUMN MODELS
# ------------------------
@dataclass
class LoanFeeColumnEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class LoanFeeColumnKeys:
    COLS: str = "cols"


class LoanFeeColumnEntry(BaseResponse):
    ADD_KEYS = [LoanFeeColumnEntryKeys.ID, LoanFeeColumnEntryKeys.LABEL, LoanFeeColumnEntryKeys.TYPE]


class LoanFeeColumnEntryList(BaseListResponse):
    SUB_MODEL = LoanFeeColumnEntry


# ROW MODELS
# ------------------------
@dataclass
class LoanFeeRowEntryKeys:
    VALUE: str = "v"


@dataclass
class LoanFeeRowColEntryKey:
    COL: str = "c"


@dataclass
class LoanFeeRowKeys:
    ROWS: str = "rows"


class LoanFeeRowEntry(BaseResponse):
    ADD_KEYS = [LoanFeeRowEntryKeys.VALUE]


class LoanFeeRowEntryList(BaseListResponse):
    SUB_MODEL = LoanFeeRowEntry


class LoanFeeRowCol(BaseResponse):
    ADD_KEYS = [LoanFeeRowColEntryKey.COL]
    SUB_MODELS = [LoanFeeRowEntryList]


class LoanFeeRowColList(BaseListResponse):
    SUB_MODEL = LoanFeeRowCol


# FULL MODEL
# ------------------------
@dataclass
class LoanFeeKeys:
    LOAN_FEES: str = "LoanFees"


class LoanFees(BaseResponse):
    ADD_KEYS = [LoanFeeColumnKeys.COLS, LoanFeeRowKeys.ROWS]
    SUB_MODELS = [LoanFeeColumnEntryList, LoanFeeRowColList]
