from PRICE.APIs.extra_data.models.extra_data import (ExtraDataEntryList, ExtraDataKeys,
                                                     ExtraDataMetadataKeys, ExtraDataMetadataEntryList)
from PRICE.base.common.response import CommonResponse


class ExtraData(CommonResponse):
    ADD_KEYS = [ExtraDataKeys.EXTRA_DATA, ExtraDataMetadataKeys.EXTRA_DATA_METADATA]
    SUB_MODELS = [ExtraDataEntryList, ExtraDataMetadataEntryList]
