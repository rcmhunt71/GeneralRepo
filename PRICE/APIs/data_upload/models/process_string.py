from dataclasses import dataclass


@dataclass
class ProcessStringKeys:
    DL_RESULT: str = "DLResult"
    LOAN_NUMBER_ID: str = "LoanNumberID"
    DATA_LANGUAGE: str = "DataLanguage"
