from dataclasses import dataclass

from PRICE.abstract.base_response import BaseListResponse
from PRICE.assets.models.asset import Asset


@dataclass
class AssetsKeys:
    ASSETS: str = 'Assets'


class Assets(BaseListResponse):
    SUB_MODEL = Asset
