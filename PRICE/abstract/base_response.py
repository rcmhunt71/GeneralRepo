import pprint

from PRICE.logger.logging import Logger

log = Logger(added_depth=1)


class ModelKeyMismatch(Exception):
    def __init__(self):
        pass


class BaseResponse:
    ADD_KEYS = None
    SUB_MODELS = None

    def __init__(self, keys=None, objs=None, **kwargs):
        self._VARS = []
        self._OBJS = []
        self.raw = kwargs
        self.model_name = self.__class__.__name__

        log.debug(f"Instantiating '{self.model_name}'")

        self._combine_args(keys=keys, objs=objs)
        log.debug(f"COMBINED PARAMETERS:\n\tself._VARS: {self._VARS}\n\tself._OBJS: {self._OBJS}")

        if self.ADD_KEYS is not None:
            # If only adding KEYS & no MODELS (nested sub-objects), create a list of NONE models
            if self.SUB_MODELS is None:
                self.SUB_MODELS = [None for _ in range(len(self.ADD_KEYS))]

            # If ADD_KEYS and SUB_MODELS provided, the number per list MUST be the same.
            elif len(self.SUB_MODELS) != len(self.ADD_KEYS):
                raise ModelKeyMismatch()

            # Number of ADD_KEYS and SUB_MODELS match, so if:
            # SUB_MODEL is None: add to KEYS to be added to base model obj.
            # SUB_MODEL is not None:
            #     * Instantiate sub_model object and add it to the kwargs
            #     * add to _OBJS to be added to base model object
            for key, model in zip(self.ADD_KEYS, self.SUB_MODELS):
                if key in kwargs and kwargs.get(key) is not None:
                    if model is not None:
                        data = kwargs.get(key)
                        kwargs[key] = model(*data) if isinstance(data, list) else model(**data)
                        self._OBJS.append(key)
                    else:
                        self._VARS.append(key)

        # Add each sub_model object or keyword to the base model object, based on what is in the **kwargs dict.
        log.debug(f"Updated KWARGS:\n{pprint.pformat(kwargs)}\n")
        for keyword, value in kwargs.items():
            if keyword in self._VARS or keyword in self._OBJS:
                setattr(self, keyword, value)
            else:
                print(f"Unrecognized argument for {self.__class__.__name__}: "
                      f"{keyword} --> Value: {value}")

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


class BaseListResponse(list):
    SUB_MODEL = None

    def __init__(self, *arg_list):
        super().__init__()
        self.model_name = self.__class__.__name__

        log.debug(f"KWARGS:\n{pprint.pformat(arg_list)}\n")
        self.raw = arg_list
        self.extend([self.SUB_MODEL(**value_dict) for value_dict in arg_list])

    def to_struct(self):
        return [elem.to_struct() for elem in self]

    def __str__(self):
        output = "\n ".join([str(elem.to_struct()) for elem in self])
        return f"[{output}]"
