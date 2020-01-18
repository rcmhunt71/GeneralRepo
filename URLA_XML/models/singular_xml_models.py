from models.singular_xml_element_base_model import BaseDealElement
from models.urla_xml_keys import UrlaXmlKeys, ElementPath


class Asset(BaseDealElement):
    """ Class definition for ASSET element """
    PATH = "/".join(ElementPath().ASSETS_PATH)
    OBJ_TYPE = UrlaXmlKeys.ASSET


class Collateral(BaseDealElement):
    """ Class definition for COLLATERAL element """
    PATH = "/".join(ElementPath().COLLATERALS_PATH)
    OBJ_TYPE = UrlaXmlKeys.COLLATERAL


class Expense(BaseDealElement):
    """ Class definition for EXPENSE element """
    PATH = "/".join(ElementPath().EXPENSES_PATH)
    OBJ_TYPE = UrlaXmlKeys.EXPENSE


class Liability(BaseDealElement):
    """ Class definition for LIABILITY element """
    PATH = "/".join(ElementPath().LIABILITIES_PATH)
    OBJ_TYPE = UrlaXmlKeys.LIABILITY


class Loan(BaseDealElement):
    """ Class definition for LOAN element """
    PATH = "/".join(ElementPath().LOANS_PATH)
    OBJ_TYPE = UrlaXmlKeys.LOAN


class Party(BaseDealElement):
    """ Class definition for PARTY element """
    PATH = "/".join(ElementPath().PARTIES_PATH)
    OBJ_TYPE = UrlaXmlKeys.PARTY

