import typing
from dataclasses import dataclass, fields

from base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class SetAntiSteeringDataKeys(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanDataKeys:
    LOAN_FIELDS: str = "LoanFields"
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


@dataclass
class SetLoanDataPayload:
    REFERRAL_SOURCE: str = "Referral_Source"
    PROGRAM_NAME: str = "Program_Name"
    PROGRAM_ID: str = "Program_ID"
    DOCUMENTATION_TYPE: str = "Documentation_Type"
    BASE_LOAN_AMOUNT: str = "Base_Loan_Amount"
    PROPERTY_TAX: str = "Property_Tax"
    ASSOCIATION_DUES: str = "Association_Dues"
    ESTIMATED_CLOSING_DATE: str = "Estimated_Closing_Date"
    NEXT_CONTACT_DATE: str = "Next_Contact_Date"
    RATE: str = "Rate"
    PROPERTY_ID: str = "Property_ID"
    LOAN_PURPOSE: str = "Loan_Purpose"
    LIEN_POSITION: str = "Lien_Position"
    NOTES: str = "Notes"
    LEAD_SOURCE: str = "Lean_Source"
    TITLE_NUMBER: str = "Title_Number"
    INTEREST_ONLY_MONTHS: str = "Interest_Only_Months"
    ESCROW_NUMBER: str = "Escrow Number"
    FIRST_PAYMENT_DATE: str = "First_Paymemt_Date"
    INVESTOR_LOAN_NUMBER: str = "Investor_Loan_Number"
    CHANNEL: str = "Channel"
    ESTIMATED_FICO: str = "EstimatedFICO"
    MI_NAME: str = "MI_Name"
    MI_PAYMENT_PERIOD: str = "MI_Payment_Period"
    MI_RENEWAL_TYPE: str = "MI_Renewal_Type"
    MORTGAGE_INSURANCE_ZERO_DUE_AT_CLOSING: str = "MortgageInsuranceZeroDueAtClosing"
    MI_COVERAGE: str = "MI_Coverage"
    LOAN_NUMBER: str = "Loan_Number"
    LENDER_ID: str = "Lender_ID"
    LOAN_OFFICER_ID: str = "Loan_Officer_ID"
    BROKER_COMPANY_ID: str = "Broker_Company_ID"
    ESCROW_COMPANY_ID: str = "Escrow_Company_ID"
    APPRAISER_COMPANY_ID: str = "Appraiser_Company_ID"
    SELLER_REALTOR_COMPANY_ID: str = "Seller_Realtor_Company_ID"
    BUYER_REALTOR_COMPANY_ID: str = "Buyer_Realtor_Company_ID"
    HAZARD_COMPANY_ID: str = "Hazard_Company_ID"
    FLOOD_COMPANY_ID: str = "Flood_Company_ID"
    MANAGEMENT_CONTACT_ID: str = "Management_Contact_ID"
    BROKER_ID: str = "Broker_ID"
    TITLE_CONTACT_ID: str = "Title_Contact_ID"
    TITLE_COMPANY_ID: str = "Title_Company_ID"
    LOAN_PROCESSOR_ID: str = "Loan_Processor_ID"
    LOAN_UNDERWRITER_ID: str = "Loan_Underwriter_ID"
    RELOCATION: str = "Relocation"
    LOCK_TYPE_ID: str = "Lock_Type_Id"
    FLOOD_ZONE: str = "Flood_Zone"
    FLOOD_NFIP_COMMUNITY_NAME: str = "FloodNFIPCommunityName"
    LOAN_FLOOD_NFIP_COMMUNITY_IDENTIFIER: str = "Loan_Flood_NFIP_Community_Identifier"
    LOAN_FLOOD_NFIP_MAP_PANEL_IDENTIFIER: str = "Loan_Flood_NFIP_Map_Panel_Identifier"
    FLOOD_NFIP_MAP_PANEL_DATE: str = "FloodNFIPMapPanelDate"
    FLOOD_NFIP_LETTER_OF_MAP_DATE: str = "FloodNFIPLetterOfMapDate"
    FLOOD_PARTIAL_INDICATOR: str = "FloodPartialIndicator"
    FLOOD_PROTECTED_AREA_DESIGNATION_DATE: str = "FloodProtectedAreaDesignationDate"
    FLOOD_LIFE_OF_LOAN_INDICATOR: str = "FloodLifeOfLoanIndicator"
    FLOOD_NFIP_COMMUNITY_PARTICIPATION_STATUS_TYPE: str = "FloodNFIPCommunityParticipationStatusType"
    LOAN_FLOOD_PRODUCT_CERTIFY_DATE: str = "Loan_Flood_Product_Certify_Date"
    HMDA_STATE: str = "HMDA_State"
    HMDA_COUNTY: str = "HMDA_County"
    HMDA_MSA: str = "HMDA_MSA"
    HMDA_CENSUS: str = "HMDA_Census"
    MERS_NUMBER: str = "Mers_Number"
    UNIVERSAL_LOAN_IDENTIFIER: str = "UniversalLoanIdentifier"
    FLOOD_CERTIFICATION_IDENTIFIER: str = "FloodCertificationIdentifier"
    FLOOD_NFIP_MAP_INDICATOR: str = "FloodNFIPMapIndicator"
    BONAFIDE_DISCOUNT_POINTS: str = "BonaFideDiscountPoints"
    UNDISCOUNTED_RATE: str = "UndiscountedRate"
    SUBORDINATE_FINANCING: str = "Subordinate_Financing"
    SUBORDINATE_RATE: str = "Subordinate_Rate"
    SUBORDINATE_TERM: str = "Subordinate_Term"
    SUBORDINATE_BALLOON: str = "Subordinate_Balloon"
    SUB_FINANCE_METHOD: str = "Sub_Finance_Method"
    MONTHLY_SUB_LIEN_PAYMENT: str = "Monthly_Sub_Lien_Payment"
    SUBORDINATE_LIEN_POSITION: str = "Subordinate_Lien_Position"
    SUB_FINANCE_HELOC_AMOUNT: str = "Sub_Finance_HELOC_Amount"
    LOAN_TERM: str = "Loan_Term"
    LOAN_TYPE: str = "Loan_Type"
    SUBMITTER_ID: str = "SubmitterID"
    SUBMITTER_PERSON_ID: str = "SubmitterPersonID"


class SetLoanDataRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id, payload_dict=None, **kwargs):

        # Kwargs are key/value pairs where a key can be a lower-case SetLoanDataPayload attribute
        # e.g. -  SUB_FINANCE_HELOC_AMOUNT -->> sub_finance_heloc_amount

        # Dynamically set all attributes based kwargs that match a SetLoanDataPayload attribute
        valid_keys = [elem.name for elem in fields(SetLoanDataPayload)]
        self.attr_list = []

        # Iterate through the kwargs
        for attr in kwargs.keys():

            # If kwargs.UPPER() matches a SetLoanDataPayload attribute, create a model attribute and store the value.
            # Also record the name of the attribute for more efficient payload generation
            if attr.upper() in valid_keys:
                setattr(self, attr.lower(), kwargs[attr])
                self.attr_list.append(attr.lower())

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        return {
            SetAntiSteeringDataKeys.SESSION_ID: self.session_id,
            SetAntiSteeringDataKeys.NONCE: self.nonce,
            SetAntiSteeringDataKeys.LOAN_NUMBER_ID: self.loan_number_id,
        }

    def build_payload(self) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        payload_list = []

        # For all recorded dynamically created attributes, create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key, None) is not None:
                payload_list.append(
                    {SetLoanDataKeys.FIELD_NAME: getattr(SetLoanDataPayload, payload_key.upper()),
                     SetLoanDataKeys.FIELD_VALUE: getattr(self, payload_key)})
        payload = {SetLoanDataKeys.LOAN_FIELDS: payload_list}
        return payload


if __name__ == "__main__":
    import pprint
    args = {
        "lock_type_id": 123,
        "flood_zone": True,
        "flood_nfip_community_name": "Rio Grande",
        "loan_flood_nfip_community_identifier": "nfip1",
        "loan_flood_nfip_map_panel_identifier": "D1C8",
    }

    obj = SetLoanDataRequest(session_id=123456, nonce=123245687, loan_number_id=986532147, **args)
    print(f"PAYLOAD: {pprint.pformat(obj.payload)}")
