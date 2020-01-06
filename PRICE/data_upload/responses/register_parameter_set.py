from PRICE.common.response import CommonResponse
from PRICE.data_upload.models.register_parameter_set import RegisterParameterSetKeys


class RegisterParameterSet(CommonResponse):
    ADD_KEYS = [RegisterParameterSetKeys.PARAMETER_SET_KEY]
    SUB_MODELS = [None]
