from dataclasses import dataclass

from PRICE.base.responses.base_response import BaseResponse
from PRICE.base.common.models.stats import StatsModel
from PRICE.base.common.models.version import VersionModel


@dataclass
class CommonResponseKeys:
    SUCCESSFUL: str = 'Successful'
    ERROR_MESSAGE: str = 'ErrorMessage'
    ERROR_CODE: str = 'ErrorCode'
    TAGS: str = 'Tags'
    NONCE: str = 'Nonce'
    STATS: str = 'Stats'
    VERSION: str = 'Version'
    RESPONDER: str = 'Responder'
    RAW_RESPONSE: str = 'raw_response'


class CommonResponse(BaseResponse):

    ADD_KEYS = [CommonResponseKeys.VERSION, CommonResponseKeys.STATS]
    SUB_MODELS = [VersionModel, StatsModel]

    def __init__(self, keys=None, objs=None, **kwargs):

        self._VARS = [CommonResponseKeys.SUCCESSFUL, CommonResponseKeys.ERROR_MESSAGE,
                      CommonResponseKeys.ERROR_CODE, CommonResponseKeys.TAGS, CommonResponseKeys.NONCE,
                      CommonResponseKeys.RESPONDER, CommonResponseKeys.RAW_RESPONSE]
        self._OBJS = [CommonResponseKeys.STATS, CommonResponseKeys.VERSION]

        self._combine_args(keys=keys, objs=objs)

        super().__init__(keys=self._VARS, objs=self._OBJS, **kwargs)

    def to_struct(self):
        response = dict([(attr, getattr(self, attr)) for attr in self._VARS if hasattr(self, attr)])
        for obj in self._OBJS:
            response[obj] = None if getattr(self, obj) is None else getattr(self, obj).to_struct()

        return response
