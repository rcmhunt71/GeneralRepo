from dataclasses import dataclass
import json


@dataclass
class BaseRequestModelKeys:
    SESSION_ID: str = "SessionID"
    NONCE: str = "Nonce"


@dataclass
class BaseRequestModel:
    def __init__(self, session_id, nonce):
        self.session_id = session_id
        self.nonce = nonce
        self.as_params_dict = self.to_params()
        self.as_json = self.to_json()

    def to_params(self):
        return {
            BaseRequestModelKeys.SESSION_ID: self.session_id,
            BaseRequestModelKeys.NONCE: self.nonce
        }

    def to_json(self):
        return json.dumps(self.to_params())
