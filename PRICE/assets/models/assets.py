from dataclasses import dataclass

from PRICE.assets.models.asset import Asset


@dataclass
class AssetsKeys:
    ASSETS: str = 'Assets'


class Assets(list):
    def __init__(self, *args):
        super().__init__()
        self.extend([Asset(**asset_dict) for asset_dict in args])

    def to_struct(self):
        return [x.to_struct() for x in self]
