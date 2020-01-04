from PRICE.common.models.stats import StatsKeys
from PRICE.common.models.version import VersionKeys
from PRICE.common.response import CommonResponseKeys
from PRICE.logger.logging import Logger

log = Logger()

version_args = {
    VersionKeys.MAJOR_VERSION: 10,
    VersionKeys.MINOR_VERSION: 20,
    VersionKeys.BUILD: 30,
    VersionKeys.HOT_FIX: 40,
}

stats_args = {
    StatsKeys.TOTAL_DATABASE_TIME: 35,
    StatsKeys.TOTAL_SERVER_TIME: 25,
    StatsKeys.METHOD_TIME: 15,
    StatsKeys.LOSTIME: 5,
}

response_args = {
    CommonResponseKeys.SUCCESSFUL: True,
    CommonResponseKeys.ERROR_MESSAGE: "Ok",
    CommonResponseKeys.ERROR_CODE: 0,
    CommonResponseKeys.TAGS: "",
    CommonResponseKeys.VERSION: version_args,
    CommonResponseKeys.STATS: stats_args,
    CommonResponseKeys.NONCE: "DEADBEEF-01234",
    CommonResponseKeys.RESPONDER: "E406F3C0BA2DDE5348F99BC0089-1224",
}


class CommonResponseValidations:
    # Class cannot be instantiated on it's own. This is multi-inheritance utility class that requires
    # co-inheritance with unittest.TestCase to function.

    def _validate_response(self, model, model_data, debug=False):

        # Only get keys with primitive values (no complex structures or objects)
        attrs = [key for key, value in model_data.items() if
                 (isinstance(value, str) or isinstance(value, int) or value is None)]

        log.debug(f"Attributes in model_data with primitives: {attrs}")

        # Verify object data matches configured data
        for attr in attrs:
            model_value = getattr(model, attr)
            data_value = model_data[attr]
            log.debug(f"Validation Assertion: {model.model_name}.{attr}: model==data ? "
                      f"('{model_value}' == '{data_value}') => {model_value == data_value}")
            self.assertEqual(model_value, data_value)
