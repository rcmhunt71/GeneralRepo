from PRICE.APIs.data_upload.models.register_parameter_set import RegisterParameterSetKeys
from PRICE.base.common.response import CommonResponse


class RegisterParameterSet(CommonResponse):
    ADD_KEYS = [RegisterParameterSetKeys.PARAMETER_SET_KEY]
    SUB_MODELS = [None]
