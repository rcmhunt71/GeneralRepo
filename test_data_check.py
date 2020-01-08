import unittest
from random import randrange, choice

from APIs.data_check.models.datacheck import DataCheckKeys, DataCheck, DataChecks, EvaluateDataCheckBundleKeys
from APIs.data_check.responses.evaluate_data_check_bundle import EvaluateDataCheckBundle
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

number_of_bundles = 3
names = ["Loan Number", "Invoice Number", "Customer ID"]
is_valid = ['valid', 'invalid']
results = ['Pass', 'Fail']


def build_data_check_data():
    return {
        DataCheckKeys.DATA_CHECK_ID: randrange(1, 99),
        DataCheckKeys.NAME: choice(names),
        DataCheckKeys.DESCRIPTION: f'The Loan Number "{randrange(1, 9999):04}" is {choice(is_valid)}',
        DataCheckKeys.RESULT: choice(results)
    }


data_check_bundle_args = [build_data_check_data() for _ in range(number_of_bundles)]


class TestDataCheck(unittest.TestCase, CommonResponseValidations):
    def test_data_check_model(self):
        index = randrange(1, number_of_bundles)
        data_check_model = DataCheck(**data_check_bundle_args[index])
        self._validate_response(model=data_check_model, model_data=data_check_bundle_args[index])

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
