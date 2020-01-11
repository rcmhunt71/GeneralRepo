from dataclasses import dataclass


@dataclass
class ForceChangePasswordKeys:
    FORCE_CHANGE_PASSWORD: str = "ForceChangePassword"


@dataclass
class PasswordAgeKeys:
    EXPIRES: str = "Expires"
    DAYS_REMAINING: str = "DaysRemaining"
    EXPIRY_NOTICE_IN_DAYS: str = "ExpiryNoticeInDays"


