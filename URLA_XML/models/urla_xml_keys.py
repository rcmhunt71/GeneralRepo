import typing
from dataclasses import dataclass, field


@dataclass
class UrlaXmlKeys:
    """
    Abstraction of MISMO v3.4 XML keywords into CONSTANTS to be used throughout application.
    This prevents hard-coding within the application, and ability to change values globally in one place.
    """
    ASSET: str = 'ASSET'
    ASSETS: str = 'ASSETS'
    ASSET_DETAIL: str = 'ASSET_DETAIL'
    ASSET_HOLDER: str = 'ASSET_HOLDER'
    COLLATERAL: str = 'COLLATERAL'
    COLLATERALS: str = 'COLLATERALS'
    DEAL_SET: str = 'DEAL_SET'
    DEAL_SETS: str = 'DEAL_SETS'
    DEAL: str = 'DEAL'
    DEALS: str = 'DEALS'
    EXPENSE: str = 'EXPENSE'
    EXPENSES: str = 'EXPENSES'
    LIABILITIES: str = 'LIABILITIES'
    LIABILITY: str = 'LIABILITY'
    LOAN: str = 'LOAN'
    LOANS: str = 'LOANS'
    MESSAGE: str = 'MESSAGE'
    PARTY: str = 'PARTY'
    PARTIES: str = 'PARTIES'
    RELATIONSHIP: str = 'RELATIONSHIP'
    RELATIONSHIPS: str = "RELATIONSHIPS"
    SEQ_NUM: str = '@SequenceNumber'
    XLINK_LABEL: str = '@xlink:label'


@dataclass
class ElementPath:
    """
    Predefined paths to specific MISMO v3.4. elements, using the UrlaXmlKeys CONSTANTS.
    """
    ASSETS_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.ASSETS])
    COLLATERALS_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.COLLATERALS])
    EXPENSES_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.EXPENSES])
    LIABILITIES_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.LIABILITIES])
    LOANS_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.LOANS])
    PARTIES_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.PARTIES])
    RELATIONSHIPS_PATH: typing.List[str] = field(
        default_factory=lambda: [UrlaXmlKeys.MESSAGE, UrlaXmlKeys.DEAL_SETS, UrlaXmlKeys.DEAL_SET, UrlaXmlKeys.DEALS,
                                 UrlaXmlKeys.DEAL, UrlaXmlKeys.RELATIONSHIPS])
