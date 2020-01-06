import unittest

from PRICE.dates.models.dates import DateKeys, DateEntry, DatesList, DatesListKeys
from PRICE.dates.responses.get_dates import GetDates
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

date_data_1 = {
    DateKeys.DATE_VALUE: "2016-01-20T00:00:00.000",
    DateKeys.DATE_NAME: "Application Received",
}

date_data_2 = {
    DateKeys.DATE_VALUE: "2019-11-21T11:11:11.010",
    DateKeys.DATE_NAME: "Application Denied",
}

dates_data = [date_data_1, date_data_2]


class TestDates(unittest.TestCase, CommonResponseValidations):
    def test_date_model(self):
        date_model = DateEntry(**date_data_1)
        self._validate_response(model=date_model, model_data=date_data_1)

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