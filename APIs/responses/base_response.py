import pprint


class BaseResponse:

    def __init__(self, keys=None, objs=None, **kwargs):
        self._VARS = []
        self._OBJS = []

        self._combine_args(keys=keys, objs=objs)

        for kw, value in kwargs.items():
            if kw in self._VARS or kw in self._OBJS:
                setattr(self, kw, value)
            else:
                print(f"Unrecognized argument for {self.__class__.__name__}: {kw} --> Value: {value}")

    def to_struct(self):
        return dict([(attr, getattr(self, attr)) for attr in self._VARS])

    def _combine_args(self, keys=None, objs=None):
        if keys is not None:
            self._VARS.extend(keys)
            self._VARS = list(set(self._VARS))

        if objs is not None:
            self._OBJS.extend(objs)
            self._OBJS = list(set(self._OBJS))

    def __str__(self):
        return pprint.pformat(self.to_struct())
