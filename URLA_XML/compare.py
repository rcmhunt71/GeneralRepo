import argparse
import json
import os
import pprint
import typing
from collections import OrderedDict
from dataclasses import dataclass, field

import xmltodict


class CLIArgs:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._defined_args()
        self.args = self.parser.parse_args()

    def _defined_args(self):
        self.parser.add_argument(
            "-s", "--source", required=True,
            help="Source XML file to use for comparison to other MISMO formatted XML files")
        self.parser.add_argument(
            "-c", "--compare", required=True,
            help="MISMO formatted XML file to verify against source XML file")
        self.parser.add_argument(
            "-o", "--outfile", action="store_true",
            help="[OPTIONAL] Create outfile of XML to dict conversion processes (for debugging)")


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
        self.data = self.convert_xml_to_dict(source_file)

    @staticmethod
    def read_file(filename: str) -> typing.List[str]:
        print(f"Reading file: {filename}")
        with open(filename, "r") as FILE:
            return FILE.readlines()

    @classmethod
    def convert_xml_to_dict(cls, filename: str):  # -> typing.OrderedDict: (not supported in Python 3.7)
        if not os.path.exists(filename):
            raise FileNotFoundError(f"XML Source file ('{filename}') was not found.")

        file_contents = cls.read_file(filename)
        return xmltodict.parse("\n".join(file_contents))

    @staticmethod
    def dump_data_to_file(outfile: str, data_dict) -> typing.NoReturn:
        with open(outfile, "w") as OUT:
            OUT.writelines(data_dict)
        print(f"Wrote to OUTFILE: {outfile} --> Created Successfully? {os.path.exists(outfile)}")

    def _get_nested_subdict(self, keys_list: typing.List[str]):  # -> typing.OrderedDict: Not supported in Python 3.7
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

    def __init__(self, data, index: int = None, path: str = None) -> typing.NoReturn:
        self.data = data

        if not isinstance(data, OrderedDict):
            print(f"DATA:\n{data}")
            print(f"INDEX: {index}")
            print(f"TYPE: {type(data)}")

        self.index = index
        self.type = self.TYPE
        self.seq_num = data.get(UrlaXmlKeys.SEQ_NUM, "NOT_SET")
        self.name = data.get(UrlaXmlKeys.XLINK_LABEL, "NOT SET")
        self.path = path or f"//{self.DELIMITER.join(self._build_xpath())}({UrlaXmlKeys.XLINK_LABEL}={self.name})"
        self.id_set = self.build_id_set()

    def _build_xpath(self) -> typing.List:
        xpath = [self.PATH]
        elem_type = self.type if self.index is None else f"{self.type}[{self.index}]"
        xpath.append(elem_type)
        return xpath

    def build_id_set(self) -> typing.Set:
        return set(self._build_id_list())

    def _build_id_list(self, key: str = None, data_set=None, tag: str = None) -> typing.List:
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

    @staticmethod
    def check_value_list(data_value):
        return data_value if isinstance(data_value, list) else [data_value]


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


def _build_out_filename(directory, filename, extension):
    filename = filename.split(os.path.sep)[-1]
    filename = f"{'.'.join(filename.split('.')[:-1])}.{extension}"
    return os.path.sep.join(['.', directory, filename])


def write_debug_files(source_obj, compare_obj, cli_args):
    if cli_args.outfile:
        OUT_DIR = 'outfiles'
        FILE_EXT = 'debug'
        INDENT, WIDTH = (4, 180)

        out_primary_filespec = _build_out_filename(directory=OUT_DIR, filename=cli_args.source, extension=FILE_EXT)
        out_compare_filespec = _build_out_filename(directory=OUT_DIR, filename=cli_args.compare, extension=FILE_EXT)

        primary_dict_info = pprint.pformat(json.dumps(source_obj.data), indent=INDENT, width=WIDTH, compact=False)
        compare_dict_info = pprint.pformat(json.dumps(compare_obj.data), indent=INDENT, width=WIDTH, compact=False)

        source_obj.dump_data_to_file(outfile=out_primary_filespec, data_dict=primary_dict_info)
        compare_obj.dump_data_to_file(outfile=out_compare_filespec, data_dict=compare_dict_info)


if __name__ == '__main__':
    cli = CLIArgs()

    source = URLA_XML(source_file=cli.args.source)
    compare = URLA_XML(source_file=cli.args.compare)

    write_debug_files(source_obj=source, compare_obj=compare, cli_args=cli.args)

    assets_dict = source.get_assets_list()
    liabilities_dict = source.get_liabilities_list()
    expenses_dict = source.get_expenses_list()
    loan_dict = source.get_loans_list()
    party_dict = source.get_parties_list()
    collat_dict = source.get_collaterals_list()

    print()
    deal_lists = [
        [Asset(data=asset_data, index=idx) for idx, asset_data in
         enumerate(Asset.check_value_list(assets_dict.get(UrlaXmlKeys.ASSET)))],
        [Liability(data=liab_data, index=idx) for idx, liab_data in
         enumerate(Liability.check_value_list(liabilities_dict.get(UrlaXmlKeys.LIABILITY)))],
        # [Expense(data=exp_data, index=idx) for idx, exp_data in
        #  enumerate(Expense.check_value_list(expenses_dict.get(UrlaXmlKeys.EXPENSE)))],  ## <-- ERROR
        [Loan(data=loan_data, index=idx) for idx, loan_data in
         enumerate(Loan.check_value_list(loan_dict.get(UrlaXmlKeys.LOAN)))],
        [Party(data=party_data, index=idx) for idx, party_data in
         enumerate(Party.check_value_list(party_dict.get(UrlaXmlKeys.PARTY)))],
        [Collateral(data=collat_data, index=idx) for idx, collat_data in
         enumerate(Collateral.check_value_list(collat_dict.get(UrlaXmlKeys.COLLATERAL)))],
    ]

    target_index = 1

    for obj_list in deal_lists:
        for index, obj in enumerate(obj_list):
            if index == target_index - 1 and index < len(obj_list):
                print(f"({index}): {obj.type} [NAME = {obj.name}]\n"
                      f"\tPATH: {obj.path}\n"
                      f"\tID_SET: {obj.id_set}\n"
                      f"\tDATA: {pprint.pformat(obj.data)}\n")
        print()


