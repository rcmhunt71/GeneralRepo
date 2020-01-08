from APIs.loans.models.final_value import FinalValueFieldsKeys, FinalValueScreenKeys
from base.common.response import CommonResponse


class GetFinalValueTags(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [FinalValueScreenKeys.FINAL_VALUE_SCREEN, FinalValueFieldsKeys.FINAL_VALUE_FIELD]

        super().__init__(keys=self._VARS, **kwargs)

    def get_final_value_screens(self):
        return getattr(self, FinalValueScreenKeys.FINAL_VALUE_SCREEN)

    def get_final_value_fields(self):
        return getattr(self, FinalValueFieldsKeys.FINAL_VALUE_FIELD)
