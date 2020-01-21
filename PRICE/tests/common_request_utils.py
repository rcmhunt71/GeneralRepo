from PRICE.logger.logging import Logger

log = Logger()


class RequestValidationTools:
    def validate_payload(self, expected_dict, actual_dict):
        expected_keys = list(k for k, v in expected_dict.items() if v is not None)
        actual_keys = list(actual_dict.keys())

        log.debug(f"Validating payload: Expected Keys == Actual Keys -> {expected_keys} <=> {actual_keys}")
        self.assertEqual(expected_keys, actual_keys)

        expected_values = [expected_dict[k] for k in expected_keys if expected_dict[k] is not None]
        actual_values = [actual_dict[k] for k in expected_keys]

        log.debug(f"Validating payload: Expected Values == Actual Values -> {expected_values} <=> {actual_values}")
        self.assertEqual(expected_values, actual_values)
