from dataclasses import dataclass

from APIs.responses.base_response import BaseResponse
from APIs.responses.models.stats import Stats as StatsModel
from APIs.responses.models.version import Version as VersionModel


@dataclass
class ResponseKeys:
    SUCCESSFUL: str = 'Successful'
    ERROR_MESSAGE: str = 'ErrorMessage'
    ERROR_CODE: str = 'ErrorCode'
    TAGS: str = 'Tags'
    NONCE: str = 'Nonce'
    STATS: str = 'Stats'
    VERSION: str = 'Version'
    RESPONDER: str = 'Responder'
    RAW_RESPONSE: str = 'raw_response'


class Response(BaseResponse):

    def __init__(self, keys=None, objs=None, **kwargs):

        self._VARS = [ResponseKeys.SUCCESSFUL, ResponseKeys.ERROR_MESSAGE, ResponseKeys.ERROR_CODE,
                      ResponseKeys.TAGS, ResponseKeys.NONCE, ResponseKeys.RESPONDER, ResponseKeys.RAW_RESPONSE]
        self._OBJS = [ResponseKeys.STATS, ResponseKeys.VERSION]

        self._combine_args(keys=keys, objs=objs)

        if kwargs.get(ResponseKeys.VERSION) is not None:
            kwargs[ResponseKeys.VERSION] = VersionModel(**kwargs.get(ResponseKeys.VERSION))
        if kwargs.get(ResponseKeys.STATS) is not None:
            kwargs[ResponseKeys.STATS] = StatsModel(**kwargs.get(ResponseKeys.STATS))

        super().__init__(keys=self._VARS, objs=self._OBJS, **kwargs)

    def to_struct(self):
        response = dict([(attr, getattr(self, attr)) for attr in self._VARS if hasattr(self, attr)])
        for obj in self._OBJS:
            response[obj] = None if getattr(self, obj) is None else getattr(self, obj).to_struct()

        return response
