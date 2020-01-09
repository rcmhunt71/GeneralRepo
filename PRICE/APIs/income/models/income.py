from dataclasses import dataclass

from PRICE.base.abstract.base_response import BaseResponse, BaseListResponse


@dataclass
class IncomeEntryKeys:
    CUSTOMER_ID: str = "CustomerID"
    INCOME_ID: str = "IncomeID"
    COMPANY_ID: str = "CompanyID"
    INCOME_TYPE: str = "IncomeType"
    TITLE_POSITION: str = "TitlePosition"
    BASE_INCOME: str = "BaseIncome"
    OVERTIME: str = "Overtime"
    BONUSES: str = "Bonuses"
    COMMISSION: str = "Commission"
    OTHER: str = "Other"
    OTHER_DESCRIPTION: str = "OtherDescription"
    TOTAL: str = "Total"
    START_DATE: str = "StartDate"
    END_DATE: str = "EndDate"
    YEARS_AT_JOB: str = "YearsAtJob"


@dataclass
class IncomeKeys:
    INCOMES: str = "Incomes"


@dataclass
class AddIncomeKeys:
    INCOME_ID: str = "IncomeID"


class IncomeEntry(BaseResponse):
    ADD_KEYS = [IncomeEntryKeys.CUSTOMER_ID, IncomeEntryKeys.INCOME_ID, IncomeEntryKeys.COMPANY_ID,
                IncomeEntryKeys.INCOME_TYPE, IncomeEntryKeys.TITLE_POSITION, IncomeEntryKeys.BASE_INCOME,
                IncomeEntryKeys.OVERTIME, IncomeEntryKeys.BONUSES, IncomeEntryKeys.COMMISSION, IncomeEntryKeys.OTHER,
                IncomeEntryKeys.OTHER_DESCRIPTION, IncomeEntryKeys.TOTAL, IncomeEntryKeys.START_DATE,
                IncomeEntryKeys.END_DATE, IncomeEntryKeys.YEARS_AT_JOB]
    SUB_MODELS = [None for _ in range(len(ADD_KEYS))]


class IncomeEntries(BaseListResponse):
    SUB_MODEL = IncomeEntry
