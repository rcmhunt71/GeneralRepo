from APIs.credit.models.import_credit_report import ImportCreditReportKeys
from base.common.response import CommonResponse


class ImportCreditReport(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED]
        super().__init__(keys=self._VARS, **kwargs)
