import unittest

from PRICE.common.models.stats import StatsModel
from PRICE.common.models.version import VersionModel
from PRICE.common.response import CommonResponse
from PRICE.tests.common_response_args import response_args, version_args, stats_args, CommonResponseValidations


# ---------------------------------------------------------------
#     TEST COMMON RESPONSE
# ---------------------------------------------------------------
class TestCommonResponse(unittest.TestCase, CommonResponseValidations):
    def test_common_response(self):
        self._validate_response(model=CommonResponse(**response_args), model_data=response_args)

    def test_version_model(self):
        self._validate_response(model=VersionModel(**version_args), model_data=version_args)

    def test_stats_model(self):
        self._validate_response(model=StatsModel(**stats_args), model_data=stats_args)


if __name__ == '__main__':
    unittest.main()
