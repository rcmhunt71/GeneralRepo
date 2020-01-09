from PRICE.APIs.loans.models.final_value import FinalValueFieldsKeys, FinalValueScreenKeys
from PRICE.base.common.response import CommonResponse


class GetFinalValueTags(CommonResponse):
    ADD_KEYS = [FinalValueScreenKeys.FINAL_VALUE_SCREEN, FinalValueFieldsKeys.FINAL_VALUE_FIELD]
    SUB_MODELS = [None, None]

    def get_final_value_screens(self):
        return getattr(self, FinalValueScreenKeys.FINAL_VALUE_SCREEN)

    def get_final_value_fields(self):
        return getattr(self, FinalValueFieldsKeys.FINAL_VALUE_FIELD)
