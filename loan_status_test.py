from PRICE.common.models.stats import StatsKeys
from PRICE.common.models.version import VersionKeys
from PRICE.common.response import CommonResponseKeys
from PRICE.loans.models.loan_status import LoanStatusKeys, LoanStatus, LoanStatuses
from PRICE.loans.responses.get_loan_statuses import GetLoanStatuses


version_args = {
    VersionKeys.MAJOR_VERSION: 10,
    VersionKeys.MINOR_VERSION: 20,
    VersionKeys.BUILD: 30,
    VersionKeys.HOT_FIX: 40,
}

stats_args = {
    StatsKeys.TOTAL_DATABASE_TIME: 35,
    StatsKeys.TOTAL_SERVER_TIME: 25,
    StatsKeys.METHOD_TIME: 15,
    StatsKeys.LOSTIME: 5,
}

response_args = {
    CommonResponseKeys.SUCCESSFUL: True,
    CommonResponseKeys.ERROR_MESSAGE: "Ok",
    CommonResponseKeys.ERROR_CODE: 0,
    CommonResponseKeys.TAGS: "",
    CommonResponseKeys.VERSION: version_args,
    CommonResponseKeys.STATS: stats_args,
    CommonResponseKeys.NONCE: "DEADBEEF-01234",
    CommonResponseKeys.RESPONDER: "E406F3C0BA2DDE5348F99BC0089-1224",
}

status_data_1 = {
    LoanStatusKeys.F_LOAN_NUMBER_ID: 2546,
    LoanStatusKeys.F_LOAN_STATUS: "Application",
}

status_data_2 = {
    LoanStatusKeys.F_LOAN_NUMBER_ID: 8675309,
    LoanStatusKeys.F_LOAN_STATUS: "Denied",
}

status_data_3 = {
    LoanStatusKeys.F_LOAN_NUMBER_ID: 55884466,
    LoanStatusKeys.F_LOAN_STATUS: "Approved",
}

statuses_data = [status_data_1, status_data_2, status_data_3]

full_status_data = response_args.copy()
full_status_data[LoanStatusKeys.LOAN_STATUSES] = statuses_data

# --- TEST ---
loan_status_obj = LoanStatus(**status_data_1)
print(f"LOAN STATUS OBJ: {loan_status_obj}\n")

loan_statuses_obj = LoanStatuses(*statuses_data)
print(f"LOAN STATUSES OBJ:\n{loan_statuses_obj}\n")

loan_status_resp = GetLoanStatuses(**full_status_data)
print(loan_status_resp)