from dataclasses import dataclass

from PRICE.base.abstract.base_response import BaseResponse, BaseListResponse


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


class LoanListHeaderEntries(BaseResponse):
    ADD_KEYS = [LoanListHeaderEntryKeys.ID, LoanListHeaderEntryKeys.LABEL, LoanListHeaderEntryKeys.TYPE]
    SUB_MODELS = [None for _ in range(len(ADD_KEYS))]


class LoanHeaderList(BaseListResponse):
    SUB_MODEL = LoanListHeaderEntries


# ============================
# --------- ROWS -------------
# ============================
@dataclass
class LoanListRowValueKeys:
    VALUE: str = "v"


@dataclass
class LoanListRowsKey:
    ROWS: str = "rows"


class LoanListRowValuesList(BaseListResponse):
    SUB_MODEL = LoanListRowValueKeys


# ============================
# -------- TABLE -------------
# ============================
@dataclass
class CustomerLoanListKeys:
    CUSTOMER_LOAN: str = "CustomerLoan"


class CustomerLoanList(BaseResponse):
    ADD_KEYS = [LoanListHeaderColumnKeys.COLS, LoanListRowsKey.ROWS]
    SUB_MODELS = [LoanListHeaderEntries, LoanListRowValuesList]
