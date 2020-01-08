import unittest

from APIs.notification.models.email import EmailMergeKeys, EmailConvLogKeys
from APIs.notification.responses.merge_email_template import MergeEmailTemplate
from APIs.notification.responses.send_email_and_make_conv_log import SendEmailAndMakeConvLog
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

# --------------------------------------------------
#             EMAIL NOTIFICATION TEST DATA
# --------------------------------------------------
email_status = {
    EmailMergeKeys.SUBJECT: "Test Subject",
    EmailMergeKeys.BODY: "Blah Blah Blah"
}

email_memo_id = {EmailConvLogKeys.MEMO_ID: 1}


# --------------------------------------------------
#             EMAIL NOTIFICATION TESTS
# --------------------------------------------------
class TestEmailAPIs(unittest.TestCase, CommonResponseValidations):
    def test_MergeEmailTemplate_response(self):
        merge_data = response_args.copy()
        merge_data.update(email_status)

        email_merge_resp = MergeEmailTemplate(**merge_data)

        for attr in email_status.keys():
            self._verify(
                descript=f"{email_merge_resp.model_name}: '{attr}' are identical",
                actual=getattr(email_merge_resp, attr), expected=email_status[attr])
        self._validate_response(model=email_merge_resp, model_data=merge_data)

    def test_SendEmailAndMakeConvLog_response(self):
        merge_data = response_args.copy()
        merge_data.update(email_memo_id)

        send_email_resp = SendEmailAndMakeConvLog(**merge_data)

        for attr in email_memo_id.keys():
            self._verify(
                descript=f"{send_email_resp.model_name}: '{attr}' are identical",
                actual=getattr(send_email_resp, attr), expected=email_memo_id[attr])
        self._validate_response(model=send_email_resp, model_data=merge_data)


if __name__ == '__main__':
    unittest.main()
