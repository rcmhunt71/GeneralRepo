from APIs.responses.models.assets import AssetsKeys, Assets
from APIs.responses.common_response import Response


class AssetsResponse(Response):

    def __init__(self, keys=None, objs=None, **kwargs):

        self._OBJS = [AssetsKeys.ASSETS]
        self._combine_args(keys=keys, objs=objs)

        if kwargs.get(AssetsKeys.ASSETS) is not None:
            kwargs[AssetsKeys.ASSETS] = Assets(*kwargs.get(AssetsKeys.ASSETS))

        super().__init__(objs=self._OBJS, **kwargs)
