import typing
from dataclasses import dataclass, fields

from base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class SetLoanHDMARequestKeys(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanHDMADataKeys:
    LOAN_HDMA_FIELDS: str = "LoanHDMAFields"
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


@dataclass
class SetLoanHDMAPayload:
    HMDA_STATE: str = "HMDAState"
    HMDA_COUNTY: str = "HMDACounty"
    HMDA_MSA: str = "HMDAMSA"
    HMDA_CENSUS: str = "HMDACensus"
    HMDA_2018_LOAN_PURPOSE_OVERRIDE: str = "HMDA2018LoanPurposeOverride"
    HMDA_2018_DENIAL_REASON_1: str = "HMDA2018DenialReason1"
    HMDA_2018_DENIAL_REASON_2: str = "HMDA2018DenialReason2"
    HMDA_2018_DENIAL_REASON_3: str = "HMDA2018DenialReason3"
    HMDA_2018_DENIAL_REASON_4: str = "HMDA2018DenialReason4"
    HMDA_2018_DENIAL_REASON_OTHER: str = "HMDA2018DenialReasonOther"
    HMDA_2018_INTRODUCTORY_RATE_PERIOD: str = "HMDA2018IntroductoryRatePeriod"
    HMDA_2018_NMLS_ID: str = "HMDA2018NMLSID"
    HMDA_2018_AUS_DECISION: str = "HMDA2018AUSDecisison"
    HMDA_2018_AUS_DECISION_OTHER: str = "HMDA2018AUSDecisisonOther"
    HMDA_LOCK: str = "HMDALock"


class SetLoanHDMARequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id, payload_dict=None, **kwargs):

        # Kwargs are key/value pairs where a key can be a lower-case SetLoanHDMAPayload attribute
        # e.g. -  HDMA_2018_NMLS_ID -->> hdma_2018_nmls_id

        # Dynamically set all attributes based kwargs that match a SetLoanDataPayload attribute
        valid_keys = [elem.name for elem in fields(SetLoanHDMAPayload)]
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
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        return {
            SetLoanHDMARequestKeys.SESSION_ID: self.session_id,
            SetLoanHDMARequestKeys.NONCE: self.nonce,
            SetLoanHDMARequestKeys.LOAN_NUMBER_ID: self.loan_number_id,
        }

    def build_payload(self) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        payload_list = []

        # For all recorded dynamically created attributes, create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key, None) is not None:
                payload_list.append(
                    {SetLoanHDMADataKeys.FIELD_NAME: getattr(SetLoanHDMAPayload, payload_key.upper()),
                     SetLoanHDMADataKeys.FIELD_VALUE: getattr(self, payload_key)})
        payload = {SetLoanHDMADataKeys.LOAN_HDMA_FIELDS: payload_list}
        return payload


if __name__ == "__main__":
    import pprint
    args = {
        "hmda_2018_denial_reason_1": "This is reason #1",
        "hmda_2018_denial_reason_2": "This is reason #2",
        "hmda_2018_denial_reason_3": "This is reason #3",
        "hmda_2018_denial_reason_4": "This is reason #4",
    }

    obj = SetLoanHDMARequest(session_id=123456, nonce=123245687, loan_number_id=986532147, **args)
    print(f"PAYLOAD: {pprint.pformat(obj.payload)}")
