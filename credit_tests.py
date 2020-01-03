from PRICE.common.models.stats import StatsKeys
from PRICE.common.models.version import VersionKeys
from PRICE.common.response import CommonResponseKeys
from PRICE.credit.models.credit_report_import_ready import CreditReportImportReadyKeys
from PRICE.credit.models.import_credit_report import ImportCreditReportKeys
from PRICE.credit.responses.import_credit_report import ImportCreditReport
from PRICE.credit.responses.is_credit_report_import_ready import CreditReportImportReady

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

import_ready_args = response_args.copy()
import_ready_args[CreditReportImportReadyKeys.READY_TO_IMPORT] = True

import_ready_response = CreditReportImportReady(**import_ready_args)
print(f"OBJ:\n{import_ready_response}")
print(f"Is credit report import ready? "
      f"{getattr(import_ready_response, CreditReportImportReadyKeys.READY_TO_IMPORT)}\n")

import_report_args = response_args.copy()
import_report_args[ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED] = False
import_report_response = ImportCreditReport(**import_report_args)
print(f"OBJ:\n{import_report_response}")
print(f"Was credit report imported? "
      f"{getattr(import_report_response, ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED)}\n")
