from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse


@dataclass
class AssetKeys:
    CUSTOMER_ID: str = 'CustomerID'
    ASSET_ID: str = 'AssetID'
    ASSET_NAME: str = 'AssetName'
    ASSET_TYPE: str = 'AssetType'
    MARKET_VALUE: str = 'MarketValue'
    FIX_DESCRIPTION: str = 'FixDescription'
    INSURANCE_FACE_VALUE: str = 'InsuranceFaceValue'
    VERIFY: str = 'Verify'
    VERIFY_DATE: str = 'VerifyDate'
    BOTH: str = 'Both'
    LIQUID: str = 'Liquid'
    RETIREMENT_FUND_DETAIL: str = 'RetirementFundDetail'


class Asset(BaseResponse):
    ADD_KEYS = [AssetKeys.CUSTOMER_ID, AssetKeys.ASSET_ID, AssetKeys.ASSET_NAME, AssetKeys.ASSET_TYPE,
                AssetKeys.MARKET_VALUE, AssetKeys.FIX_DESCRIPTION, AssetKeys.INSURANCE_FACE_VALUE,
                AssetKeys.VERIFY, AssetKeys.VERIFY_DATE, AssetKeys.BOTH, AssetKeys.LIQUID,
                AssetKeys.RETIREMENT_FUND_DETAIL, ]
