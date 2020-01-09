from PRICE.base.common.response import CommonResponse
from PRICE.APIs.income.models.income import AddIncomeKeys


class AddIncome(CommonResponse):
    ADD_KEYS = [AddIncomeKeys.INCOME_ID]
    SUB_MODELS = [None]
