from PRICE.common.response import CommonResponse
from PRICE.credit.models.credit_report_import_ready import CreditReportImportReadyKeys


class CreditReportImportReady(CommonResponse):
    ADD_KEYS = [CreditReportImportReadyKeys.READY_TO_IMPORT]
    SUB_MODELS = [None]
