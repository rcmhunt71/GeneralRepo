import unittest
from random import randrange, choice

from PRICE.deposit.models.deposit import DepositKeys, Deposit, DepositsKeys, Deposits
from PRICE.deposit.models.deposit_account import (DepositAccountKeys, DepositAccount,
                                                  DepositAccounts, DepositAccountsKeys)
from PRICE.deposit.responses.get_deposit_accounts import GetDepositAccounts
from PRICE.deposit.responses.get_deposits import GetDeposits
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

YES_NO = ["Yes", "No"]
ACCOUNT_TYPES = ["Checking", "Savings", "CD", "Escrow"]
NUMBER_OF_DATA_ELEM = 3


def build_deposit_data_format():
    return {DepositKeys.CUSTOMER_ID: randrange(4455669985),
            DepositKeys.DEPOSIT_ID: randrange(1122334455),
            DepositKeys.INSTITUTION_ID: randrange(5566884423),
            DepositKeys.VERIFY: choice(YES_NO),
            DepositKeys.VERIFY_DATA: f"{randrange(9999):04}-{randrange(99):02}-{randrange(99):02}",
            DepositKeys.BOTH: choice(YES_NO)}


deposits_data = [build_deposit_data_format() for _ in range(NUMBER_OF_DATA_ELEM)]


def build_deposit_account_format():
    return {DepositAccountKeys.CUSTOMER_ID: randrange(1122344566),
            DepositAccountKeys.DEPOSIT_ID: randrange(10),
            DepositAccountKeys.DEPOSIT_ACCOUNT_ID: randrange(10),
            DepositAccountKeys.ACCOUNT_TYPE: choice(ACCOUNT_TYPES),
            DepositAccountKeys.ACCOUNT_NUMBER: "",
            DepositAccountKeys.BALANCE: randrange(9999999)}


deposit_accounts_data = [build_deposit_account_format() for _ in range(NUMBER_OF_DATA_ELEM)]


class TestDepositAccount(unittest.TestCase, CommonResponseValidations):
    def test_deposit_account_model(self):
        deposit_acct_model = DepositAccount(**deposit_accounts_data[0])
        self._validate_response(model=deposit_acct_model, model_data=deposit_accounts_data[0])

    def test_deposit_accounts_list_model(self):
        deposit_accts_list_model = DepositAccounts(*deposit_accounts_data)

        self._verify(descript=f"{deposit_accts_list_model.model_name}: has correct number of elements in list",
                     actual=len(deposit_accts_list_model), expected=len(deposit_accounts_data))

        for index, sub_model in enumerate(deposit_accts_list_model):
            self._validate_response(model=sub_model, model_data=deposit_accounts_data[index])

    def test_GetDepositAccounts_response(self):
        dep_key = DepositAccountsKeys.DEPOSIT_ACCOUNTS

        dep_args = response_args.copy()
        dep_args[dep_key] = deposit_accounts_data
        dep_accts_resp = GetDepositAccounts(**dep_args)

        self._verify(descript=f"{dep_accts_resp.model_name}: has '{dep_key}' attribute",
                     actual=hasattr(dep_accts_resp, dep_key), expected=True)
        self._validate_response(model=dep_accts_resp, model_data=dep_args)


class TestDeposits(unittest.TestCase, CommonResponseValidations):
    def test_deposit_model(self):
        deposit_model = Deposit(**deposits_data[0])
        self._validate_response(model=deposit_model, model_data=deposits_data[0])

    def test_deposits_list_model(self):
        deposit_list_model = Deposits(*deposits_data)

        self._verify(descript=f"{deposit_list_model.model_name}: has correct number of elements in list",
                     actual=len(deposit_list_model), expected=len(deposits_data))

        for index, sub_model in enumerate(deposit_list_model):
            self._validate_response(model=sub_model, model_data=deposits_data[index])

    def test_GetDeposits_response(self):
        dep_key = DepositsKeys.DEPOSITS

        dep_args = response_args.copy()
        dep_args[dep_key] = deposits_data
        deposits_resp = GetDeposits(**dep_args)

        self._verify(descript=f"{deposits_resp.model_name}: has '{dep_key}' attribute",
                     actual=hasattr(deposits_resp, dep_key), expected=True)
        self._validate_response(model=deposits_resp, model_data=dep_args)


if __name__ == '__main__':
    unittest.main()

