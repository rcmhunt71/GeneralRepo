#!/usr/bin/env python

from PRICE.assets.responses.add_automobile import AddAutomobileResponse
from PRICE.assets.models.asset import AssetKeys, Asset
from PRICE.assets.models.assets import AssetsKeys, Assets
from PRICE.assets.responses.get_assets import AssetsResponse
from PRICE.assets.models.automobile import AutomobileKeys

from PRICE.common.models.stats import Stats, StatsKeys
from PRICE.common.models.version import Version, VersionKeys
from PRICE.common.response import CommonResponse, CommonResponseKeys

from PRICE.company.responses.add_company import AddCompanyResponse
from PRICE.company.responses.get_companies import GetCompaniesResponse
from PRICE.company.models.company import CompanyKeys, Company
from PRICE.company.models.companies import CompaniesKeys, Companies
from PRICE.company.responses.get_company_ids import GetCompanyIDsResponse, GetCompanyIDsKeys

from PRICE.configuration.configuration_list import ConfigurationList, ConfigurationListKeys

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

company_ids = [
    123,
    456,
    789,
    98,
    333,
    777
]

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

assets = [asset_1, asset_2]
companies = [company_args_1, company_args_2]

# ---------------------------------------------------------------
#   VALIDATION SECTION
# ---------------------------------------------------------------
asset_obj = Asset(**asset_1)
print(f"ASSET OBJ:\n{asset_obj}")

assets_obj = Assets(*assets)
print(f"ASSETS OBJ:\n{assets_obj}")

stats = Stats(**stats_args)
print(f"STATS:\n{stats}")

version = Version(**version_args)
print(f"VERSION:\n{version}")

response = CommonResponse(**response_args)
print(f"RESPONSE:\n{response}")

config_args = response_args.copy()
config_args[ConfigurationListKeys.CONFIGURATION_LIST] = config_list
configuration = ConfigurationList(**config_args)
print(f"CONFIGURATION LIST:\n{configuration}")
print(f"Major Version: {configuration.Version.MajorVersion} sec")
print(f"Hotfix Version: {configuration.Version.Hotfix} sec")
print(f"Total Server Time: {configuration.Stats.TotalServerTime} sec")
print(f"2nd Element in Config List: '{configuration.ConfigurationList[1]}'\n")

assets_args = response_args.copy()
assets_args[AssetsKeys.ASSETS] = assets
assets_list = AssetsResponse(**assets_args)
print(f"ASSETS LIST:\n{assets_list}")
print(f"RFD of 1st ASSET: '{assets_list.Assets[0].RetirementFundDetail}'")


car_id = "CAR-123"
automobile_args = response_args.copy()
automobile_args[AutomobileKeys.AUTOMOBILE_ID] = car_id
auto = AddAutomobileResponse(**automobile_args)
print(f"AUTO LIST:\n{auto}")
print(f"Auto ID: {auto.AutomobileID}")

add_company_args = response_args.copy()
company = AddCompanyResponse(**add_company_args)
print(f"ADD COMPANY:\n{company}")

company_data = Company(**company_args_1)
print(f"Company:\n{company_data}")

companies_data = Companies(*companies)
print(f"Companies:\n{companies_data}")
print(f"DATA: {companies_data[0].CompanyName}")

get_company_args = response_args.copy()
get_company_args[CompaniesKeys.COMPANIES] = companies
companies_resp = GetCompaniesResponse(**get_company_args)
print(f"Companies:\n{companies_resp}")
print(f"DATA: {companies_resp.Companies[1].CompanyName}")

company_ids_args = response_args.copy()
company_ids_args[GetCompanyIDsKeys.COMPANY_IDS] = company_ids
company_ids_response = GetCompanyIDsResponse(**company_ids_args)
print(f"COMPANY ID LIST:\n{company_ids_response}")
print(f"COMPANY ID #3:\n{company_ids_response.CompanyIds[2]}")