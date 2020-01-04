import unittest

from PRICE.assets.models.asset import AssetKeys, Asset
from PRICE.assets.models.assets import AssetsKeys, Assets
from PRICE.assets.models.automobile import AutomobileKeys
from PRICE.assets.responses.add_automobile import AddAutomobileResponse
from PRICE.assets.responses.get_assets import AssetsResponse
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# ---------------------------------------------------------------
#     ASSET TEST DATA
# ---------------------------------------------------------------
asset_1 = {
    AssetKeys.CUSTOMER_ID: 123456,
    AssetKeys.ASSET_ID: "A-123456",
    AssetKeys.ASSET_NAME: "TestAsset1",
    AssetKeys.ASSET_TYPE: "Test",
    AssetKeys.MARKET_VALUE: "10000",
    AssetKeys.FIX_DESCRIPTION: "Broken",
    AssetKeys.INSURANCE_FACE_VALUE: "10000",
    AssetKeys.VERIFY: True,
    AssetKeys.VERIFY_DATE: "20200101",
    AssetKeys.BOTH: True,
    AssetKeys.LIQUID: False,
    AssetKeys.RETIREMENT_FUND_DETAIL: "Blah Blah Blah",
}

asset_2 = {
    AssetKeys.CUSTOMER_ID: 987654,
    AssetKeys.ASSET_ID: "A-987654",
    AssetKeys.ASSET_NAME: "TestAsset2",
    AssetKeys.ASSET_TYPE: "Test1",
    AssetKeys.MARKET_VALUE: "1000000",
    AssetKeys.FIX_DESCRIPTION: "FIXED",
    AssetKeys.INSURANCE_FACE_VALUE: "1000000",
    AssetKeys.VERIFY: False,
    AssetKeys.VERIFY_DATE: "20000101",
    AssetKeys.BOTH: False,
    AssetKeys.LIQUID: True,
    AssetKeys.RETIREMENT_FUND_DETAIL: "Yadda Yadda Yadda",
}

assets_list = [asset_1, asset_2]


# ---------------------------------------------------------------
#   ASSET TESTS
# ---------------------------------------------------------------
class TestAssets(unittest.TestCase, CommonResponseValidations):
    def test_asset_model(self):
        asset_obj = Asset(**asset_1)
        for key in asset_1.keys():
            self.assertEqual(getattr(asset_obj, key), asset_1[key])

    def test_assets_model(self):
        self._test_assets_model(model=Assets(*assets_list), keys=asset_1.keys())

    def test_assets_response(self):
        assets_args = response_args.copy()
        assets_args[AssetsKeys.ASSETS] = assets_list
        assets_list_resp = AssetsResponse(**assets_args)

        self.assertTrue(hasattr(assets_list_resp, AssetsKeys.ASSETS))

        model = getattr(assets_list_resp, AssetsKeys.ASSETS)
        self._test_assets_model(model=model, keys=asset_1.keys())
        self._validate_response(model=assets_list_resp, model_data=assets_args)

    def test_automobile_response(self):
        key = AutomobileKeys.AUTOMOBILE_ID

        automobile_args = response_args.copy()
        automobile_args[key] = "CAR-123"
        auto = AddAutomobileResponse(**automobile_args)

        self._validate_response(model=auto, model_data=automobile_args)

    def _test_assets_model(self, model, keys):
        self.assertEqual(len(assets_list), len(model))
        for index, asset in enumerate(assets_list):
            for key in keys:
                self.assertEqual(getattr(model[index], key), assets_list[index][key])


if __name__ == "__main__":
    unittest.main()
