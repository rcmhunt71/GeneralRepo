from dataclasses import dataclass

from PRICE.abstract.base_response import BaseResponse


@dataclass
class VersionKeys:
    MAJOR_VERSION: str = 'MajorVersion'
    MINOR_VERSION: str = 'MinorVersion'
    HOT_FIX: str = 'Hotfix'
    BUILD: str = 'Build'


class Version(BaseResponse):

    def __init__(self, **kwargs):
        self._VARS = [VersionKeys.MAJOR_VERSION, VersionKeys.MINOR_VERSION, VersionKeys.HOT_FIX,
                      VersionKeys.BUILD]

        super().__init__(keys=self._VARS, **kwargs)

    def full_version(self):
        return (f"{getattr(self, VersionKeys.MAJOR_VERSION)}.{getattr(self, VersionKeys.MINOR_VERSION)}."
                f"{getattr(self, VersionKeys.BUILD)}.{getattr(self, VersionKeys.HOT_FIX)}")
