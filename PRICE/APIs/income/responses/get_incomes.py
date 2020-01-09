from PRICE.APIs.income.models.income import IncomeEntries, IncomeKeys
from PRICE.base.common.response import CommonResponse


class GetIncomes(CommonResponse):
    ADD_KEYS = [IncomeKeys.INCOMES]
    SUB_MODELS = [IncomeEntries]
