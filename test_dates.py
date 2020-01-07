import unittest
from random import choice, randrange

from PRICE.dates.models.dates import DateKeys, DateEntry, DatesList, DatesListKeys
from PRICE.dates.responses.get_dates import GetDates
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

number_dates = 3
status = ["Received", "Denied"]


def build_date_data():
    return {
        DateKeys.DATE_VALUE: f"{randrange(2005, 2018)}-{randrange(1-12):02}-{randrange(1-28):02}T"
                             f"{randrange(0-24):02}:{randrange(0, 60):02}:{randrange(0, 60)}.{randrange(999):03}",
        DateKeys.DATE_NAME: f"Application {choice(status)}",
    }


dates_data = [build_date_data() for _ in range(number_dates)]


class TestDates(unittest.TestCase, CommonResponseValidations):
    def test_date_model(self):
        index = randrange(number_dates)
        date_model = DateEntry(**dates_data[index])
        self._validate_response(model=date_model, model_data=dates_data[index])

    def test_dates_model(self):
        dates_model = DatesList(*dates_data)
        self._verify(descript=f"{dates_model.model_name}: has correct number of elements",
                     actual=len(dates_model), expected=len(dates_data))

    def test_get_dates_response(self):
        dates_args = response_args.copy()
        dates_args[DatesListKeys.DATES_LIST] = dates_data
        get_dates_resp = GetDates(**dates_args)
        self._validate_response(model=get_dates_resp, model_data=dates_args)


if __name__ == '__main__':
    unittest.main()
