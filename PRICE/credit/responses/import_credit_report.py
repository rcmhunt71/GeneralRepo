from PRICE.common.response import CommonResponse
from PRICE.credit.models.import_credit_report import ImportCreditReportKeys


class ImportCreditReport(CommonResponse):
    def __init__(self, **kwargs):
        self._VARS = [ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED]
        super().__init__(keys=self._VARS, **kwargs)
