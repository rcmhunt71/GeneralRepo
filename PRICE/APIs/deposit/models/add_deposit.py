from dataclasses import dataclass


@dataclass
class AddDepositKeys:
    DEPOSIT_ID: str = "DepositID"
    DEPOSIT_ACCOUNT_ID: str = "DepositAcccountID"
