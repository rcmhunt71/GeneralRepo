from PRICE.APIs.password.models.password import PasswordAgeKeys
from PRICE.base.common.response import CommonResponse


class GetEmployeePasswordAge(CommonResponse):
    ADD_KEYS = [PasswordAgeKeys.EXPIRES, PasswordAgeKeys.DAYS_REMAINING, PasswordAgeKeys.EXPIRY_NOTICE_IN_DAYS]
    SUB_MODELS = [None, None, None]
