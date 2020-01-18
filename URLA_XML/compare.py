from collections import OrderedDict
from dataclasses import dataclass, field
import json
import os
import pprint
import typing

import xmltodict


@dataclass
class UrlaXmlKeys:
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


class URLA_XML:
    def __init__(self, source_file):
        self.source_file = source_file
        self.data = self.convert_xml_to_dict(XML_SOURCE)

    @staticmethod
    def read_file(filename: str) -> typing.List[str]:
        print(f"Reading file: {filename}")
        with open(filename, "r") as FILE:
            return FILE.readlines()

    @classmethod
    def convert_xml_to_dict(cls, filename: str) -> typing.OrderedDict:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"XML Source file ('{filename}') was not found.")

        file_contents = cls.read_file(filename)
        return xmltodict.parse("\n".join(file_contents))

    @staticmethod
    def dump_data_to_file(outfile: str, data_dict: typing.OrderedDict) -> typing.NoReturn:
        with open(outfile, "w") as OUT:
            OUT.writelines(data_dict)
        print(f"Wrote to OUTFILE: {outfile} Created? {os.path.exists(outfile)}")

    def _get_nested_subdict(self, keys_list: typing.List[str]) -> typing.OrderedDict:
        data_subset = self.data
        for key in keys_list:
            if key in data_subset:
                data_subset = data_subset.get(key)
                print(f"\tFound key: {key} --> Key Sequence: {keys_list} --> Next set of keys: {data_subset.keys()}")
            else:
                print(f"\tKey not found: {key} --> Requested Key Sequence: {keys_list}")
                break
        return data_subset

    def get_assets_list(self):
        return self._get_element_family(family=UrlaXmlKeys.ASSETS)

    def get_liabilities_list(self):
        return self._get_element_family(family=UrlaXmlKeys.LIABILITIES)

    def get_loans_list(self):
        return self._get_element_family(family=UrlaXmlKeys.LOANS)

    def get_collaterals_list(self):
        return self._get_element_family(family=UrlaXmlKeys.COLLATERALS)

    def get_expenses_list(self):
        return self._get_element_family(family=UrlaXmlKeys.EXPENSES)

    def get_relationships_list(self):
        return self._get_element_family(family=UrlaXmlKeys.RELATIONSHIPS)

    def get_parties_list(self):
        return self._get_element_family(family=UrlaXmlKeys.PARTIES)

    def _get_element_family(self, family):
        return self._get_nested_subdict(keys_list=getattr(ElementPath(), f"{family.upper()}_PATH"))


class BaseDealElement:
    PATH = 'NOT SET'
    DELIMITER = "/"
    TYPE = "UNKNOWN"

    def __init__(self, data: typing.OrderedDict, index: int = None, path: str = None) -> typing.NoReturn:
        self.data = data
        self.index = index
        self.type = self.TYPE
        self.seq_num = data.get(UrlaXmlKeys.SEQ_NUM, "NOT_STE")
        self.name = data.get(UrlaXmlKeys.XLINK_LABEL, "NOT SET")
        self.path = path or f"//{self.DELIMITER.join(self._build_xpath())}({UrlaXmlKeys.XLINK_LABEL}={self.name})"
        self.id_set = self.build_id_set()

    def _build_xpath(self) -> typing.List:
        xpath = [self.PATH]
        if self.index is not None:
            xpath[-1] += f"[{self.index}]"
        xpath.append(self.type)
        return xpath

    def build_id_set(self) -> typing.Set:
        return set(self._build_id_list())

    def _build_id_list(self, key: str = None, data_set: typing.OrderedDict = None, tag=None) -> typing.List:
        """
        Recursively traverses the OrderDict, building a list of path strings. The path strings are the colon-delimited
        paths and final value.

        Example of a path string: "{tag1}:{tag2}:{tag3}:value"

        :param key: Current Key in parent OrderDict to process (used to build path tag).
        :param data_set: Current value in parent_keys OrderDict to process
        :param tag: Current tag (from parent call), current key will be appended.

        :return: list of "path_tag:<...>:value" strings

        """
        # Determine the data set.
        # If it is not provided (provided when an iterative call), start with the object's initial data
        data_set = data_set if data_set is not None else self.data

        # Determine the list of parent keys.
        # If the list is not provided (from iterative calls), start with the object's initial OrderedDict keys.
        parent_keys = [key] if key is not None else [x for x in self.data.keys()]

        # The list to accumulate and return
        set_data = []

        # Iterate through the parent keys, decomposing the structure of each corresponding value.
        for p_key in parent_keys:

            # Ignore all labels (prefixed with @, e.g. - @xlink:label)
            if p_key.startswith('@'):
                continue

            # Get the data (dict value) associated with the key
            asset_data = data_set.get(p_key, data_set)

            # Build the tag. The tag is the prefix/path to the value.
            tag = p_key if tag is None else f"{tag}:{p_key}"

            # Accumulate all non-label elements that have values (not dictionaries)
            set_data.extend([f"{tag}:{key}:{value}" for key, value in asset_data.items() if
                             not isinstance(value, OrderedDict) and not key.startswith('@')])

            # Recursively process all OrderDicts in current data set and add results.
            for key, value in asset_data.items():
                if isinstance(value, OrderedDict):
                    set_data.extend(self._build_id_list(key=key, data_set=value, tag=tag))

        # return the accumulated list of tag[:tag[:tag]]:value strings
        return set_data


class Asset(BaseDealElement):
    PATH = "/".join(ElementPath().ASSETS_PATH)
    TYPE = UrlaXmlKeys.ASSET


class Collateral(BaseDealElement):
    PATH = "/".join(ElementPath().COLLATERALS_PATH)
    TYPE = UrlaXmlKeys.COLLATERAL


class Liability(BaseDealElement):
    PATH = "/".join(ElementPath().LIABILITIES_PATH)
    TYPE = UrlaXmlKeys.LIABILITY


class Expense(BaseDealElement):
    PATH = "/".join(ElementPath().EXPENSES_PATH)
    TYPE = UrlaXmlKeys.EXPENSE


class Loan(BaseDealElement):
    PATH = "/".join(ElementPath().LOANS_PATH)
    TYPE = UrlaXmlKeys.LOAN


class Party(BaseDealElement):
    PATH = "/".join(ElementPath().PARTIES_PATH)
    TYPE = UrlaXmlKeys.PARTY


if __name__ == '__main__':
    WRITE_TO_OUTFILE = False

    # Build input & output file specs
    XML_FILENAME = 'D1_CO2.xml'
    OUT_FILENAME = "D1_CO2.dict"
    SOURCE_DIR = "xml_files"
    OUT_DIR = 'outfiles'
    XML_SOURCE = os.path.sep.join(['.', SOURCE_DIR, XML_FILENAME])
    OUT_FILE = os.path.sep.join(['.', OUT_DIR, OUT_FILENAME])

    source = URLA_XML(source_file=XML_SOURCE)

    assets_dict = source.get_assets_list()
    liabilities_dict = source.get_liabilities_list()
    expenses_dict = source.get_expenses_list()

    print()
    deal_lists = [
        [Asset(data=asset_data, index=idx) for idx, asset_data in enumerate(assets_dict.get(UrlaXmlKeys.ASSET))],
        [Liability(data=liab_data, index=idx) for idx, liab_data in enumerate(liabilities_dict.get(UrlaXmlKeys.LIABILITY))],
        [Expense(data=exp_data, index=idx) for idx, exp_data in enumerate(expenses_dict.get(UrlaXmlKeys.EXPENSE))],  ## <-- ERROR
    ]

    target_index = 2

    for obj_list in deal_lists:
        for index, obj in enumerate(obj_list):
            if index == target_index - 1:
                print(f"({index}): {obj.name}\n"
                      f"\tPATH: {obj.path}\n"
                      f"\tID_SET: {obj.id_set}\n"
                      f"\tDATA: {pprint.pformat(obj.data)}\n")
        print()

    if WRITE_TO_OUTFILE:
        dict_info = pprint.pformat(json.dumps(source.data), indent=4, width=180, compact=False)
        print(f"Contents:\n{dict_info}")
        source.dump_data_to_file(outfile=OUT_FILE, data_dict=dict_info)
