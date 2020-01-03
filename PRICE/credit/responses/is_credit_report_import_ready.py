from PRICE.common.response import CommonResponse
from PRICE.credit.models.credit_report_import_ready import CreditReportImportReadyKeys


class CreditReportImportReady(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [CreditReportImportReadyKeys.READY_TO_IMPORT]
        super().__init__(keys=self._VARS, **kwargs)
