import unittest

from PRICE.data_check.models.datacheck import DataCheckKeys, DataCheck, DataChecks, EvaluateDataCheckBundleKeys
from PRICE.data_check.responses.evaluate_data_check_bundle import EvaluateDataCheckBundle
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

data_check_args_1 = {
    DataCheckKeys.DATA_CHECK_ID: 25,
    DataCheckKeys.NAME: "Loan Number",
    DataCheckKeys.DESCRIPTION: 'The Loan Number "1337" is valid',
    DataCheckKeys.RESULT: "Pass"
}

data_check_args_2 = {
    DataCheckKeys.DATA_CHECK_ID: 50,
    DataCheckKeys.NAME: "Invoice Number",
    DataCheckKeys.DESCRIPTION: 'The Invoice Number "8856" is invalid',
    DataCheckKeys.RESULT: "Fail"
}

data_check_args_3 = {
    DataCheckKeys.DATA_CHECK_ID: 75,
    DataCheckKeys.NAME: "Customer ID",
    DataCheckKeys.DESCRIPTION: 'The Customer ID is "L337" is valid',
    DataCheckKeys.RESULT: "Pass"
}

data_check_bundle_args = [data_check_args_1, data_check_args_2, data_check_args_3]


class TestDataCheck(unittest.TestCase, CommonResponseValidations):
    def test_data_check_model(self):
        data_check_model = DataCheck(**data_check_args_1)
        self._validate_response(model=data_check_model, model_data=data_check_args_1)

    def test_data_checks_model(self):
        data_checks_model = DataChecks(*data_check_bundle_args)
        self._verify(descript=f"{data_checks_model.model_name}: "
                              f"has correct number of {data_checks_model.SUB_MODEL} instances",
                     actual=len(data_checks_model), expected=len(data_check_bundle_args))

        for sub_model, model_data in zip(data_checks_model, data_check_bundle_args):
            self._validate_response(model=sub_model, model_data=model_data)

    def test_evaluate_data_checks_response(self):
        attr = EvaluateDataCheckBundleKeys.DATA_CHECKS

        data_args = response_args.copy()
        data_args[attr] = data_check_bundle_args
        eval_data_resp = EvaluateDataCheckBundle(**data_args)

        self._verify(descript=f"{eval_data_resp.model_name}: has {attr}",
                     actual=hasattr(eval_data_resp, attr), expected=True)

        self._verify(descript=f"{eval_data_resp.model_name}: {attr} is a list",
                     actual=isinstance(getattr(eval_data_resp, attr), list), expected=True)

        self._validate_response(model=eval_data_resp, model_data=data_args)


if __name__ == '__main__':
    unittest.main()
