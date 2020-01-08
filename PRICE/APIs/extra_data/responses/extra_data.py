from PRICE.APIs.extra_data.models.extra_data import (ExtraDataEntryList, ExtraDataKeys,
                                                     ExtraDataMetadataKeys, ExtraDataMetadataEntryList)
from PRICE.base.common.response import CommonResponse


class ExtraData(CommonResponse):
    def __init__(self, keys=None, objs=None, **kwargs):

        key_models = [(ExtraDataKeys.EXTRA_DATA, ExtraDataEntryList),
                      (ExtraDataMetadataKeys.EXTRA_DATA_METADATA, ExtraDataMetadataEntryList)]

        objs = objs or []

        for (key, model) in key_models:
            if key in kwargs:
                objs.append(key)
                kwargs[key] = model(*kwargs.get(key))

        super().__init__(keys=keys, objs=objs, **kwargs)
