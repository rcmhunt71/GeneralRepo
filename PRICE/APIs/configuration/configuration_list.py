from dataclasses import dataclass

from base.common.response import CommonResponse


@dataclass
class ConfigurationListKeys:
    CONFIGURATION_LIST: str = "ConfigurationList"


class ConfigurationList(CommonResponse):

    def __init__(self, **kwargs):
        self._VARS = [ConfigurationListKeys.CONFIGURATION_LIST]
        super().__init__(keys=self._VARS, **kwargs)
