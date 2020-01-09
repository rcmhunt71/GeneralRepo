from PRICE.APIs.credit.models.import_credit_report import ImportCreditReportKeys
from PRICE.base.common.response import CommonResponse


class ImportCreditReport(CommonResponse):
    ADD_KEYS = [ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED]
    SUB_MODELS = [None]
