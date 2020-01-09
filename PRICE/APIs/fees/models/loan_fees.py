from dataclasses import dataclass

from PRICE.base.abstract.base_response import BaseResponse, BaseListResponse


@dataclass
class LoanFeeColumnEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class LoanFeeColumnKeys:
    COLS: str = "cols"


@dataclass
class LoanFeeRowKeys:
    ROWS: str = "rows"


@dataclass
class LoanFeeRowEntryKeys:
    VALUE: str = "v"


@dataclass
class LoanFeeKeys:
    LOAN_FEES: str = "LoanFees"


# COLUMN MODELS
# ------------------------
class LoanFeeColumnEntry(BaseResponse):
    ADD_KEYS = [LoanFeeColumnEntryKeys.ID, LoanFeeColumnEntryKeys.LABEL, LoanFeeColumnEntryKeys.TYPE]


class LoanFeeColumnEntryList(BaseListResponse):
    SUB_MODEL = LoanFeeColumnEntry


# ROW MODELS
# ------------------------


# FULL MODEL
# ------------------------
class LoanFees(BaseResponse):

    # TODO: Add LoanFee Row Keys Model
    def __init__(self, keys=None, objs=None, **kwargs):

        key_models = [(LoanFeeColumnKeys.COLS, LoanFeeColumnEntryList),
                      (LoanFeeRowKeys.ROWS, None)]

        objs = objs or []

        for (key, model) in key_models:
            if key in kwargs:
                objs.append(key)
                kwargs[key] = model(*kwargs.get(key))

        super().__init__(keys=keys, objs=objs, **kwargs)
