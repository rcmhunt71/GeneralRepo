from dataclasses import dataclass

from PRICE.APIs.assets.models.asset import Asset
from PRICE.base.responses.base_response import BaseListResponse


@dataclass
class AssetsKeys:
    ASSETS: str = 'Assets'


class Assets(BaseListResponse):
    SUB_MODEL = Asset
