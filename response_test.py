#!/usr/bin/env python
import pprint

from PRICE.assets.responses.add_automobile import AddAutomobileResponse
from PRICE.assets.models.asset import AssetKeys, Asset
from PRICE.assets.models.assets import AssetsKeys, Assets
from PRICE.assets.responses.get_assets import AssetsResponse
from PRICE.assets.models.automobile import AutomobileKeys

from PRICE.common.models.stats import StatsModel, StatsKeys
from PRICE.common.models.version import VersionModel, VersionKeys
from PRICE.common.response import CommonResponse, CommonResponseKeys

from PRICE.company.responses.add_company import AddCompanyResponse
from PRICE.company.responses.get_companies import GetCompaniesResponse
from PRICE.company.models.company import CompanyKeys, Company
from PRICE.company.models.companies import CompaniesKeys, Companies
from PRICE.company.responses.get_company_ids import GetCompanyIDsResponse, GetCompanyIDsKeys

from PRICE.configuration.configuration_list import ConfigurationList, ConfigurationListKeys

from PRICE.loans.responses.add_loan import AddLoanKeys, AddLoan, GetLoan
from PRICE.loans.responses.get_final_value_tags import GetFinalValueTags
from PRICE.loans.models.final_value import FinalValueFieldsKeys, FinalValueScreenKeys
from PRICE.loans.models.loan_data import (DataTableColumnEntryKeys, DataRowValueKeys, DataTableKeys, DataColumnEntry,
                                          DataCols, RowValueEntry, RowColsValue, DataRowColKeys, RowEntry, RowList,
                                          DataTable)

# ---------------------------------------------------------------
#     TEST DATA
# ---------------------------------------------------------------

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

config_list = [
    "Mr.",
    "Mrs.",
    "Ms.",
    "Miss",
    "Dr.",
]

company_ids_list = [
    123,
    456,
    789,
    98,
    333,
    777
]

loan_id = "8675309"

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

asset_1 = {
    AssetKeys.CUSTOMER_ID: 123456,
    AssetKeys.ASSET_ID: "A-123456",
    AssetKeys.ASSET_NAME: "TestAsset1",
    AssetKeys.ASSET_TYPE: "Test",
    AssetKeys.MARKET_VALUE: "10000",
    AssetKeys.FIX_DESCRIPTION: "Broken",
    AssetKeys.INSURANCE_FACE_VALUE: "10000",
    AssetKeys.VERIFY: True,
    AssetKeys.VERIFY_DATE: "20200101",
    AssetKeys.BOTH: True,
    AssetKeys.LIQUID: False,
    AssetKeys.RETIREMENT_FUND_DETAIL: "Blah Blah Blah",
}

asset_2 = {
    AssetKeys.CUSTOMER_ID: 987654,
    AssetKeys.ASSET_ID: "A-987654",
    AssetKeys.ASSET_NAME: "TestAsset2",
    AssetKeys.ASSET_TYPE: "Test1",
    AssetKeys.MARKET_VALUE: "1000000",
    AssetKeys.FIX_DESCRIPTION: "FIXED",
    AssetKeys.INSURANCE_FACE_VALUE: "1000000",
    AssetKeys.VERIFY: False,
    AssetKeys.VERIFY_DATE: "20000101",
    AssetKeys.BOTH: False,
    AssetKeys.LIQUID: True,
    AssetKeys.RETIREMENT_FUND_DETAIL: "Yadda Yadda Yadda",
}

company_args_1 = {
    CompanyKeys.COMPANY_ID: 'CMP111',
    CompanyKeys.COMPANY_NAME: 'Test Company 1',
    CompanyKeys.VOICE: '5558004673',
    CompanyKeys.ADDRESS: "123 SomePlace Drive",
    CompanyKeys.CITY: "Albany",
    CompanyKeys.STATE: "NY",
    CompanyKeys.ZIP: 78108,
}

company_args_2 = {
    CompanyKeys.COMPANY_ID: 'CMP222',
    CompanyKeys.COMPANY_NAME: 'Test Company 2',
    CompanyKeys.VOICE: '5558004674',
    CompanyKeys.ADDRESS: "978 SomeWhere Lane",
    CompanyKeys.CITY: "San Diego",
    CompanyKeys.STATE: "CA",
    CompanyKeys.ZIP: 87404,
}

final_screen_list = [1024]
final_fields_list = ['Test1', 'Test2']

assets_list = [asset_1, asset_2]
companies_list = [company_args_1, company_args_2]

data_column_args_1 = {
    DataTableColumnEntryKeys.ID: "Loan_Number_ID",
    DataTableColumnEntryKeys.LABEL: "Loan Number ID",
    DataTableColumnEntryKeys.TYPE: "number",
}

data_column_args_2 = {
    DataTableColumnEntryKeys.ID: "Status_ID",
    DataTableColumnEntryKeys.LABEL: "Status ID",
    DataTableColumnEntryKeys.TYPE: "number",
}

data_columns_list = [data_column_args_1, data_column_args_2]

value_entry_1 = {DataRowValueKeys.VALUE: 4}
value_entry_2 = {DataRowValueKeys.VALUE: 7}

value_entry_3 = {DataRowValueKeys.VALUE: 40}
value_entry_4 = {DataRowValueKeys.VALUE: 70}


col_values_list_1 = [value_entry_1, value_entry_2]
col_values_list_2 = [value_entry_3, value_entry_4]

col_value_dict_1 = {DataRowColKeys.COL: col_values_list_1}
col_value_dict_2 = {DataRowColKeys.COL: col_values_list_2}

row_datum_1 = [col_value_dict_1, col_value_dict_2]

data_table = {DataTableKeys.COLS: data_columns_list,
              DataTableKeys.ROWS: row_datum_1}

# ---------------------------------------------------------------
#   VALIDATION SECTION
# ---------------------------------------------------------------
asset_obj = Asset(**asset_1)
print(f"ASSET OBJ:\n{asset_obj}")

assets_obj = Assets(*assets_list)
print(f"ASSETS OBJ:\n{assets_obj}")

stats = StatsModel(**stats_args)
print(f"STATS:\n{stats}")

version = VersionModel(**version_args)
print(f"VERSION:\n{version}")

response = CommonResponse(**response_args)
print(f"RESPONSE:\n{response}")
print(f"RESPONSE BUILD_ID: {response.Version.full_version_info()}\n")

config_args = response_args.copy()
config_args[ConfigurationListKeys.CONFIGURATION_LIST] = config_list
configuration = ConfigurationList(**config_args)
print(f"CONFIGURATION LIST:\n{configuration}")
print(f"Major Version: {configuration.Version.MajorVersion} sec")
print(f"Hotfix Version: {configuration.Version.Hotfix} sec")
print(f"Total Server Time: {configuration.Stats.TotalServerTime} sec")
print(f"2nd Element in Config List: '{configuration.ConfigurationList[1]}'\n")

assets_args = response_args.copy()
assets_args[AssetsKeys.ASSETS] = assets_list
assets_list_resp = AssetsResponse(**assets_args)
print(f"ASSETS LIST:\n{assets_list_resp}")
print(f"RFD of 1st ASSET: '{assets_list_resp.Assets[0].RetirementFundDetail}'\n")


car_id = "CAR-123"
automobile_args = response_args.copy()
automobile_args[AutomobileKeys.AUTOMOBILE_ID] = car_id
auto = AddAutomobileResponse(**automobile_args)
print(f"AUTO LIST:\n{auto}")
print(f"Auto ID: {auto.AutomobileID}\n")

add_company_args = response_args.copy()
company = AddCompanyResponse(**add_company_args)
print(f"ADD COMPANY:\n{company}\n")

company_data = Company(**company_args_1)
print(f"Company:\n{company_data}\n")

companies_data = Companies(*companies_list)
print(f"Companies:\n{companies_data}")
print(f"DATA: {companies_data[0].CompanyName}\n")

get_company_args = response_args.copy()
get_company_args[CompaniesKeys.COMPANIES] = companies_list
companies_resp = GetCompaniesResponse(**get_company_args)
print(f"Companies:\n{companies_resp}")
print(f"DATA: {companies_resp.Companies[1].CompanyName}\n")

company_ids_args = response_args.copy()
company_ids_args[GetCompanyIDsKeys.COMPANY_IDS] = company_ids_list
company_ids_response = GetCompanyIDsResponse(**company_ids_args)
print(f"COMPANY ID LIST:\n{company_ids_response}")
print(f"COMPANY ID #3:\n{company_ids_response.CompanyIds[2]}\n")

add_loan_args = response_args.copy()
add_loan_args[AddLoanKeys.NEW_LOAN_NUMBER_ID] = loan_id
add_loan_response = AddLoan(**add_loan_args)
print(f"ADD LOAN RESPONSE:\n{add_loan_response}")
print(f"NEW LOAN ID: {add_loan_response.get_loan_id()}\n")

get_fv_tags_args = response_args.copy()
get_fv_tags_args[FinalValueScreenKeys.FINAL_VALUE_SCREEN] = final_screen_list
get_fv_tags_args[FinalValueFieldsKeys.FINAL_VALUE_FIELD] = final_fields_list
fb_tags_resp = GetFinalValueTags(**get_fv_tags_args)
print(fb_tags_resp)
print(f"FIELD VALUES: {fb_tags_resp.get_final_value_fields()}")
print(f"FIELD SCREENS: {fb_tags_resp.get_final_value_screens()}\n")

dc_resp = DataColumnEntry(**data_column_args_1)
print(f"DATA COLUMN ENTRY: {dc_resp}\n")

dc_cols_resp = DataCols(*data_columns_list)
print(f"DATA COLS:\n{dc_cols_resp}\n")

val_resp = RowValueEntry(**value_entry_1)
print(f"ROW DATA VALUE: {val_resp}\n")

val_col_resp = RowColsValue(*col_values_list_1)
print(f"DATA ROW LISTS:\n{val_col_resp}\n")

key = RowEntry.ADD_KEYS[0]
val_col_dict_resp = RowEntry(**col_value_dict_1)
print(f"COL DICT --> Key = '{key}':\n{getattr(val_col_dict_resp, key)}\n")

row_data_resp = RowList(*row_datum_1)
print(f"ROW COLUMN LIST DATA, FIRST ELEMENT:\n{row_data_resp[0].c}")
print(f"ROW COLUMN LIST DATA, SECOND ELEMENT:\n{row_data_resp[1].c}")

data_table_resp = DataTable(**data_table)
print(f"DATA LABEL: {data_table_resp.cols[1].id}")
print(f"DATA LABEL: {data_table_resp.rows[1].c[1].v}")

get_loan_data = response_args.copy()
get_loan_data[DataTableKeys.DATA_TABLE] = data_table

print(f"Data Table:\n{pprint.pformat(data_table)}\n")
print(f"GET LOAN DATA:\n{pprint.pformat(get_loan_data)}\n")

get_loan_resp = GetLoan(**get_loan_data)
print(f"VERSION: {get_loan_resp.Version.full_version_info()}")
print(f"Has Data Element: {hasattr(get_loan_resp, DataTableKeys.DATA_TABLE)}")
print(f"get_loan_resp.Data.rows[0].c[1].v: {get_loan_resp.Data.rows[0].c[0].v}")
print(f"get_loan_resp.Data.rows[1].c[2].v: {get_loan_resp.Data.rows[1].c[0].v}")
