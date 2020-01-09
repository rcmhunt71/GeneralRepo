from dataclasses import dataclass

from PRICE.base.abstract.base_response import BaseResponse, BaseListResponse


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
    def __init__(self, keys=None, objs=None, **kwargs):

        key_models = [(LoanFeeColumnKeys.COLS, LoanFeeColumnEntryList),
                      (LoanFeeRowKeys.ROWS, LoanFeeRowColList)]

        objs = objs or []

        for (key, model) in key_models:
            if key in kwargs:
                objs.append(key)
                kwargs[key] = model(*kwargs.get(key))

        super().__init__(keys=keys, objs=objs, **kwargs)
