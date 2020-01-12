from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse, BaseListResponse


# ============================
# -------- COLUMNS -----------
# ============================
@dataclass
class LoanListHeaderEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class LoanListHeaderColumnKeys:
    COLS: str = "cols"


class LoanListHeaderEntry(BaseResponse):
    ADD_KEYS = [LoanListHeaderEntryKeys.ID, LoanListHeaderEntryKeys.LABEL, LoanListHeaderEntryKeys.TYPE]
    SUB_MODELS = [None for _ in range(len(ADD_KEYS))]


class LoanListHeaderList(BaseListResponse):
    SUB_MODEL = LoanListHeaderEntry


# ============================
# --------- ROWS -------------
# ============================
@dataclass
class LoanListRowValueEntryKeys:
    VALUE: str = "v"


@dataclass
class LoanListRowColValueEntryKeys:
    COL: str = "c"


@dataclass
class LoanListRowsKeys:
    ROWS: str = "rows"


class LoanListRowValueEntry(BaseResponse):
    ADD_KEYS = [LoanListRowValueEntryKeys.VALUE]
    SUB_MODELS = [None]


class LoanListRowValuesList(BaseListResponse):
    SUB_MODEL = LoanListRowValueEntry


class LoanListRowCol(BaseResponse):
    ADD_KEYS = [LoanListRowColValueEntryKeys.COL]
    SUB_MODELS = [LoanListRowValuesList]


class LoanListRowColList(BaseListResponse):
    SUB_MODEL = LoanListRowCol


# ============================
# -------- TABLE -------------
# ============================
@dataclass
class CustomerLoanListKeys:
    CUSTOMER_LOAN: str = "CustomerLoan"


class CustomerLoanList(BaseResponse):
    ADD_KEYS = [LoanListHeaderColumnKeys.COLS, LoanListRowsKeys.ROWS]
    SUB_MODELS = [LoanListHeaderList, LoanListRowColList]
