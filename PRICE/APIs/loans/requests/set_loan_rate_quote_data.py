import typing
from dataclasses import dataclass, fields

from base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class SetLoanRateQuoteDataPayload:
    MI_QUOTE_VENDOR: str = "MIQuoteVendor"
    MI_PAYMENT_PERIOD: str = "MIPaymentPeriod"
    MGIC_RENEWAL_CALCULATION_TYPE: str = "MGICRenewalCalculationType"
    MI_ZERO_DUE_AT_CLOSING: str = "MIZeroDueAtClosing"
    MGIC_PREMIUM_REFUNDABLE_TYPE: str = "MGICPremiumRefundableType"
    COVERAGE: str = "Coverage"
    MGIC_PREMIUM_PAYMENT_TYPE: str = "MGICPremiumPaymentType"
    MI_SPECIAL_DEAL: str = "MISpecialDeal"
    RATE_QUOTE_ID: str = "RateQuoteID"
    MGIC_PREMIUM_RATE_PLAN_TYPE: str = "MGICPremiumRatePlanType"
    STATUS_DESCRIPTION: str = "StatusDescription"


@dataclass
class SetLoanRateQuoteDataKeys:
    LOAN_RATE_QUOTE_DETAILS: str = "LoanRateQuoteDetails"
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


@dataclass
class SetLoanQuoteRateDataRequestKeys(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    VENDOR_NAME: str = "VendorName"


class SetLoanQuoteRateDataRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id, vendor_name, payload_dict=None, **kwargs):

        # Kwargs are key/value pairs where a key can be a lower-case SetLoanHDMAPayload attribute
        # e.g. -  HDMA_2018_NMLS_ID -->> hdma_2018_nmls_id

        # Dynamically set all attributes based kwargs that match a SetLoanDataPayload attribute
        valid_keys = [elem.name for elem in fields(SetLoanRateQuoteDataPayload)]

        self.attr_list = []

        # Iterate through the kwargs
        for attr in kwargs.keys():

            # If kwargs.UPPER() matches a SetLoanHDMAPayload attribute
            # Create a model attribute and store the value.
            # Record the name of the created attribute for more efficient payload generation later in the process.
            if attr.upper() in valid_keys:
                setattr(self, attr.lower(), kwargs[attr])
                self.attr_list.append(attr.lower())

        self.loan_number_id = loan_number_id
        self.vendor_name = vendor_name
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        return {
            SetLoanQuoteRateDataRequestKeys.SESSION_ID: self.session_id,
            SetLoanQuoteRateDataRequestKeys.NONCE: self.nonce,
            SetLoanQuoteRateDataRequestKeys.LOAN_NUMBER_ID: self.loan_number_id,
            SetLoanQuoteRateDataRequestKeys.VENDOR_NAME: self.vendor_name
        }

    def build_payload(self) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        payload_list = []

        # For all recorded dynamically created attributes, create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key, None) is not None:
                payload_list.append(
                    {SetLoanRateQuoteDataKeys.FIELD_NAME: getattr(SetLoanRateQuoteDataPayload, payload_key.upper()),
                     SetLoanRateQuoteDataKeys.FIELD_VALUE: getattr(self, payload_key)})
        payload = {SetLoanRateQuoteDataKeys.LOAN_RATE_QUOTE_DETAILS: payload_list}
        return payload


if __name__ == "__main__":
    import pprint

    args = {
        "coverage": "This is coverage --> here",
        "rate_quote_id": 34537349857,
        "status_description": "This is the status_description",
    }

    def _build_payload(data_dict):
        primary_key = SetLoanRateQuoteDataKeys.LOAN_RATE_QUOTE_DETAILS
        payload_list = [{SetLoanRateQuoteDataKeys.FIELD_NAME: key,
                         SetLoanRateQuoteDataKeys.FIELD_VALUE: value} for key, value in args.items()]
        return {primary_key: payload_list}

    print("Testing SetLoanQuoteRateDataRequest - payload_dict()")
    obj_payload = SetLoanQuoteRateDataRequest(session_id=123456, nonce=123245687, vendor_name="test_vendor",
                                              loan_number_id=986532147, payload_dict=_build_payload(args))
    print(f"PAYLOAD: {pprint.pformat(obj_payload.payload)}")

    print("Testing SetLoanQuoteRateDataRequest - kwargs")
    obj_args = SetLoanQuoteRateDataRequest(session_id=123456, nonce=123245687, vendor_name="test_vendor",
                                           loan_number_id=986532147, **args)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
