from dataclasses import dataclass

from PRICE.abstract.base_response import BaseResponse


@dataclass
class StatsKeys:
    TOTAL_DATABASE_TIME: str = 'TotalDatabaseTime'
    TOTAL_SERVER_TIME: str = 'TotalServerTime'
    METHOD_TIME: str = 'MethodTime'
    LOSTIME: str = 'LOSTime'


class StatsModel(BaseResponse):

    def __init__(self, **kwargs):
        self._VARS = [StatsKeys.TOTAL_DATABASE_TIME, StatsKeys.TOTAL_SERVER_TIME, StatsKeys.METHOD_TIME,
                      StatsKeys.LOSTIME]

        super().__init__(keys=self._VARS, **kwargs)
