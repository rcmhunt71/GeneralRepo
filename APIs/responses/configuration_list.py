from dataclasses import dataclass

from APIs.responses.common_response import Response


@dataclass
class ConfigurationListKeys:
    CONFIGURATION_LIST: str = "ConfigurationList"


class ConfigurationList(Response):

    def __init__(self, **kwargs):
        self._VARS = [ConfigurationListKeys.CONFIGURATION_LIST]
        super().__init__(keys=self._VARS, **kwargs)
