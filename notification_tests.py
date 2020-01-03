from PRICE.common.models.stats import StatsKeys
from PRICE.common.models.version import VersionKeys
from PRICE.common.response import CommonResponseKeys
from PRICE.notification.models.email import EmailMergeKeys, EmailConvLogKeys
from PRICE.notification.responses.merge_email_template import MergeEmailTemplate
from PRICE.notification.responses.send_email_and_make_conv_log import SendEmailAndMakeConvLog


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

email_status = {
    EmailMergeKeys.SUBJECT: "Test Subject",
    EmailMergeKeys.BODY: "Blah Blah Blah"
}

email_memo_id = {EmailConvLogKeys.MEMO_ID: 1}

merge_data = response_args.copy()
merge_data.update(email_status)
email_merge_resp = MergeEmailTemplate(**merge_data)
print(f"Object:\n{email_merge_resp}")
for attr in [EmailMergeKeys.SUBJECT, EmailMergeKeys.BODY]:
    print(f"{attr}: '{getattr(email_merge_resp, getattr(EmailMergeKeys, attr.upper()))}'")
print()

merge_data = response_args.copy()
merge_data.update(email_memo_id)
email_merge_resp = SendEmailAndMakeConvLog(**merge_data)
print(f"Object:\n{email_merge_resp}")
for attr in ['MEMO_ID']:
    print(f"{attr}: '{getattr(email_merge_resp, getattr(EmailConvLogKeys, attr.upper()))}'")
print()
