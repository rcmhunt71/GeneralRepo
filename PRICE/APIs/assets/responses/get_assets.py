from PRICE.APIs.assets.models.assets import AssetsKeys, Assets
from PRICE.base.common.response import CommonResponse


class AssetsResponse(CommonResponse):
    ADD_KEYS = [AssetsKeys.ASSETS]
    SUB_MODELS = [Assets]
