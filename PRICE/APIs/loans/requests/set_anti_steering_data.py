import typing
from dataclasses import dataclass, fields

from base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class SetAntiSteeringDataKeys(BaseRequestModelKeys):
    ANTI_STEERING_DATA: str = "AntiSteeringData"
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetAntiSteeringDataPayload:
    INDEX: str = "Index"
    PROGRAM_ID: str = "ProgramID"
    RATE: str = "Rate"
    LOAN_ORIGINATION: str = "LoanOrigination"
    LOAN_DISCOUNT: str = "LoanDiscount"
    SALES_PRICE: str = "SalesPrice"
    VALUE: str = "Value"
    BASE_LOAN_AMOUNT: str = "BaseLoanAmount"
    OTHER_FINANCING: str = "OtherFinancing"


class SetAntiSteeringDataRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id, index=None, program_id=None, rate=None,
                 loan_origination=None, loan_discount=None, sales_price=None, value=None,
                 base_loan_amount=None, other_financing=None, payload_dict=None):

        self.loan_number_id = loan_number_id
        self.index = index
        self.program_id = program_id
        self.rate = rate
        self.loan_origination = loan_origination
        self.loan_discount = loan_discount
        self.sales_price = sales_price
        self.value = value
        self.base_loan_amount = base_loan_amount
        self.other_financing = other_financing
        self.payload = payload_dict
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        return {
            SetAntiSteeringDataKeys.SESSION_ID: self.session_id,
            SetAntiSteeringDataKeys.NONCE: self.nonce,
            SetAntiSteeringDataKeys.LOAN_NUMBER_ID: self.loan_number_id,
        }

    def build_payload(self) -> typing.Dict[str, typing.Any]:
        payload = {}
        for payload_key in [elem.name for elem in fields(SetAntiSteeringDataPayload)]:
            if getattr(self, payload_key.lower(), None) is not None:
                payload[payload_key.lower()] = getattr(self, payload_key.lower())
        return payload


if __name__ == "__main__":
    border = "-" * 80
    payload_args = {'index': 4, 'program_id': 4665, 'other_financing': False, 'rate': 0.4}
    args = {'session_id': 123456789, "nonce": 9876543210, "loan_number_id": 22446688}

    print(f"PAYLOAD AS ARGS:\n{border}")
    data = args.copy()
    data.update(payload_args)
    obj = SetAntiSteeringDataRequest(**data)
    payload_body = obj.payload
    print(f"OBJECT ARGS:\n{args}")
    print(f"PAYLOAD ARGS:\n{payload_args}")
    print(f"PAYLOAD OBJ:\n{payload_body}")

    print(f"\nPAYLOAD AS DICT:\n{border}")

    obj = SetAntiSteeringDataRequest(payload_dict=payload_args, **args)
    payload_body = obj.payload
    print(f"OBJECT ARGS:\n{args}")
    print(f"PAYLOAD ARGS:\n{payload_args}")
    print(f"PAYLOAD OBJ:\n{payload_body}")


