from dataclasses import dataclass

from PRICE.base.common.response import CommonResponse


@dataclass
class ConfigurationListKeys:
    CONFIGURATION_LIST: str = "ConfigurationList"


class ConfigurationList(CommonResponse):
    ADD_KEYS = [ConfigurationListKeys.CONFIGURATION_LIST]
    SUB_MODELS = [None]
