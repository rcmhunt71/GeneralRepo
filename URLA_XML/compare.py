import argparse
import json
import os
import pprint
import typing
from collections import OrderedDict
from dataclasses import dataclass, field

import xmltodict


class CLIArgs:
    """
    CLI Arguments available for this application.
    See _defined_args for list and description of the available arguments

    """
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
    Predefined paths to specific MISMO v3.4. elements, using the UrlaMxlKeys CONSTANTS.
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


class UrlaXML:
    """

    This class reads and converts the MISMO v3.4 XML into a complex, nested python data structure. It removes the need
    to process the XML, and allows the user to quickly access the various data elements within the XML.

    """
    def __init__(self, source_file: str):
        self.source_file = source_file
        self.data = self.convert_xml_to_dict(source_file)

    @staticmethod
    def read_file(filename: str) -> typing.List[str]:
        print(f"Reading file: {filename}")
        with open(filename, "r") as FILE:
            return FILE.readlines()

    @classmethod
    def convert_xml_to_dict(cls, filespec: str):  # -> typing.OrderedDict: (not supported in Python 3.7)
        """
        Reads XML and converts the contents to a nested collections.OrderedDict
        :param filespec: filespec of the input XML file.

        :return: OrderedDict representation of the XML.

        """
        if not os.path.exists(filespec):
            raise FileNotFoundError(f"XML Source file ('{filespec}') was not found.")

        file_contents = cls.read_file(filespec)
        return xmltodict.parse("\n".join(file_contents))

    @staticmethod
    def dump_data_to_file(outfile: str, data_dict: OrderedDict) -> typing.NoReturn:
        """
        Write the OrderedDict to file (as a string)
        :param outfile: file spec of the file to dump contents
        :param data_dict: OrderedDict to write to file

        :return: None

        """
        with open(outfile, "w") as OUT:
            OUT.writelines(data_dict)
        print(f"Wrote to OUTFILE: {outfile} --> Created Successfully? {os.path.exists(outfile)}")

    def _get_nested_subdict(self, keys_list: typing.List[str]) -> OrderedDict:
        """
        Given a list of keys (XML tags), traverse the list within the OrderedDict and return the value of the final key.

        :param keys_list: List of XML tags to traverse.

        :return: Value of the final key provided.

        """
        data_subset = self.data

        # Iterate through the list
        for key in keys_list:

            # Check if key is in the current OrderedDict.
            # Gf so, save value and prepare to check next key in the list, record error and stop.
            if key in data_subset:
                data_subset = data_subset.get(key)
                print(f"\tFound key: {key} --> Key Sequence: {keys_list} --> Next set of keys: {data_subset.keys()}")
            else:
                print(f"\tKey not found: {key} --> Requested Key Sequence: {keys_list}")
                break

        return data_subset

    def get_assets_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the ASSETS level.
        :return: List of OrderedDicts containing the ASSET data.
        """
        family = UrlaXmlKeys.ASSETS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_liabilities_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the LIABILITIES level.
        :return: List of OrderedDicts containing the LIABILITY data.
        """
        family = UrlaXmlKeys.LIABILITIES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_loans_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the LOANS level.
        :return: List of OrderedDicts containing the LOAN data.
        """
        family = UrlaXmlKeys.LOANS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_collaterals_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the COLLATERALS level.
        :return: List of OrderedDicts containing the COLLATERAL data.
        """
        family = UrlaXmlKeys.COLLATERALS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_expenses_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the EXPENSES level.
        :return: List of OrderedDicts containing the EXPENSE data.
        """
        family = UrlaXmlKeys.EXPENSES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_relationships_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the RELATIONSHIPS level.
        :return: List of OrderedDicts containing the RELATIONSHIP data.
        """
        family = UrlaXmlKeys.RELATIONSHIPS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_parties_list(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the PARTIES level.
        :return: List of OrderedDicts containing the PARTY data.
        """
        family = UrlaXmlKeys.PARTIES
        return self._check_value_is_list(self._get_element_family(family=family))

    @staticmethod
    def _check_value_is_list(data_dict: OrderedDict) -> OrderedDict:
        """
        Check if each dict value is a list. If not, put into list context.
        :param data_dict: dictionary to check if values are an instance of list
        :return: dictionary of lists
        """
        for dict_key, dict_value in data_dict.items():
            data_dict[dict_key] = dict_value if isinstance(data_dict[dict_key], list) else [dict_value]
        return data_dict

    def _get_element_family(self, family) -> OrderedDict:
        """
        Get the OrderedDict stored at the specified level.
        :return: List of OrderedDicts containing the specified data.
        """
        return self._get_nested_subdict(keys_list=getattr(ElementPath(), f"{family.upper()}_PATH"))


class BaseDealElement:
    """
    Common definition for "singular" elements as defined in MISMO v3.4. XML format.

    There is a hierarchy of tags, where under each PLURAL tag is 1+ SINGULAR tags:

      DEALS [
        DEAL {
          ASSETS [      <--- PLURAL tag
            ASSET {}    <--- SINGULAR tag
            ASSET {}    <--- SINGULAR tag
            ...
            ]
          LOANS [       <--- PLURAL tag
            LOAN {}     <--- SINGULAR tag
            LOAN {}     <--- SINGULAR tag
            ...
            ]
          EXPENSES [     <--- PLURAL tag
            EXPENSE {}   <--- SINGULAR tag
            EXPENSE {}   <--- SINGULAR tag
            ...
            ]
          ...
        }
        ...
      ]

    """

    VALUE_NOT_SET = "NOT_SET"
    XPATH_DELIMITER = "/"
    PATH = VALUE_NOT_SET
    OBJ_TYPE = VALUE_NOT_SET

    def __init__(self, data: OrderedDict, index: int = None, path: str = None) -> typing.NoReturn:
        """
        Creates base element

        :param data: OrderedDict of element definition & data
        :param index: Index in list (multiple child elements of type X can exist under DEAL element)
        :param path: xpath from XML root to element if known, otherwise it will be determined.
        """
        self.data = data

        # This condition is an error, so display the issue and the corresponding data.
        if not isinstance(data, OrderedDict):
            print(f"DATA:\n{data}\nINDEX: {index}\nPATH: {path}\nTYPE: {type(data)}")

        self.index = index
        self.type = self.OBJ_TYPE
        self.seq_num = data.get(UrlaXmlKeys.SEQ_NUM, self.VALUE_NOT_SET)
        self.name = data.get(UrlaXmlKeys.XLINK_LABEL, self.VALUE_NOT_SET)
        self.xpath = path or (f"//{self.XPATH_DELIMITER.join(self._build_xpath())}"
                              f"({UrlaXmlKeys.XLINK_LABEL}={self.name})")
        self.id_set = self.build_id_set()

    def _build_xpath(self) -> typing.List:
        """
        Determines current segment of element XPATH (including position index if in a list context).
        :return: List of tags (from ROOT (//)) to get to current element.
        """
        xpath = [self.PATH]
        elem_type = self.type if self.index is None else f"{self.type}[{self.index}]"
        xpath.append(elem_type)
        return xpath

    def build_id_set(self) -> typing.Set:
        """
        Gets list of elements to get specific value and converts to a set (guarantees uniqueness and allows quick
        comparisons between sets (e.g. - union, complement, etc.)
        """
        return set(self._build_id_list())

    def _build_id_list(self, key: str = None, data_set: OrderedDict = None, tag: str = None) -> typing.List:
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
    """ Class definition for ASSET element """
    PATH = "/".join(ElementPath().ASSETS_PATH)
    OBJ_TYPE = UrlaXmlKeys.ASSET


class Collateral(BaseDealElement):
    """ Class definition for COLLATERAL element """
    PATH = "/".join(ElementPath().COLLATERALS_PATH)
    OBJ_TYPE = UrlaXmlKeys.COLLATERAL


class Liability(BaseDealElement):
    """ Class definition for LIABILITY element """
    PATH = "/".join(ElementPath().LIABILITIES_PATH)
    OBJ_TYPE = UrlaXmlKeys.LIABILITY


class Expense(BaseDealElement):
    """ Class definition for EXPENSE element """
    PATH = "/".join(ElementPath().EXPENSES_PATH)
    OBJ_TYPE = UrlaXmlKeys.EXPENSE


class Loan(BaseDealElement):
    """ Class definition for LOAN element """
    PATH = "/".join(ElementPath().LOANS_PATH)
    OBJ_TYPE = UrlaXmlKeys.LOAN


class Party(BaseDealElement):
    """ Class definition for PARTY element """
    PATH = "/".join(ElementPath().PARTIES_PATH)
    OBJ_TYPE = UrlaXmlKeys.PARTY


def _build_out_filename(target_dir: str, input_fname: str, ext: str) -> str:
    """
    Builds the out file name, based on desired directory and extension, using the filename of the input file
    (minus the file extension)
    
    :param target_dir: (str) relative path to the directory to write the file
    :param input_fname: (str) name of input file
    :param ext: (str) file extension to append to the out file

    :return: (str) full absolute-path file spec

    """
    # Get the input filename, minus any file path (/this/direct/file.ext --> file.ext)
    input_fname = input_fname.split(os.path.sep)[-1]

    # Get the input filename, minus the extension, and append the provided extension.
    input_fname = f"{'.'.join(input_fname.split('.')[:-1])}.{ext}"

    # Build the complete file spec and return as an absolute path
    return os.path.abspath(os.path.sep.join(['.', target_dir, input_fname]))


def write_debug_files(source_obj: UrlaXML, compare_obj: UrlaXML, cli_args: argparse.Namespace) -> typing.NoReturn:
    """
    Given the UrlaXML objs, write the OrderedDict as a str (OrderedDict is output from converting XML to dict)

    :param source_obj: Source XML object
    :param compare_obj: Comparison XML object
    :param cli_args: CLI args (should the files be written, based on CLI args provided)

    :return: None

    """
    # If --outfile/-o boolean is True, create the files
    if cli_args.outfile:
        outfile_dir, outfile_ext = ('outfiles', 'out')
        indent, width = (4, 180)

        # Build file spec (filename + path)
        out_primary_file_spec = _build_out_filename(
            target_dir=outfile_dir, input_fname=cli_args.source, ext=outfile_ext)
        out_compare_file_spec = _build_out_filename(
            target_dir=outfile_dir, input_fname=cli_args.compare, ext=outfile_ext)

        # Build output data structure (as string)
        primary_dict_info = pprint.pformat(json.dumps(source_obj.data), indent=indent, width=width, compact=False)
        compare_dict_info = pprint.pformat(json.dumps(compare_obj.data), indent=indent, width=width, compact=False)

        # Write to file
        source_obj.dump_data_to_file(outfile=out_primary_file_spec, data_dict=primary_dict_info)
        compare_obj.dump_data_to_file(outfile=out_compare_file_spec, data_dict=compare_dict_info)


# ------------------------------------------------
#       MAIN SCRIPT LOGIC
# ------------------------------------------------
if __name__ == '__main__':

    # Parse CLI args
    cli = CLIArgs()

    # Create URLA XML Objects (read file, convert to nested OrderedDict structure)
    source = UrlaXML(source_file=cli.args.source)
    compare = UrlaXML(source_file=cli.args.compare)

    # Write debug files if requested
    write_debug_files(source_obj=source, compare_obj=compare, cli_args=cli.args)

    # Get lists of OrderedDicts for various elements in the source MISMO XML
    assets_dict = source.get_assets_list()
    liabilities_dict = source.get_liabilities_list()
    expenses_dict = source.get_expenses_list()
    loan_dict = source.get_loans_list()
    party_dict = source.get_parties_list()
    collat_dict = source.get_collaterals_list()

    # For dev and debug, create lists of sub-DEAL-<TAG> OrderedDicts
    print()
    deal_lists = [
        [Asset(data=asset_data, index=idx) for idx, asset_data in
         enumerate(assets_dict.get(UrlaXmlKeys.ASSET))],
        [Liability(data=liab_data, index=idx) for idx, liab_data in
         enumerate(liabilities_dict.get(UrlaXmlKeys.LIABILITY))],
        # [Expense(data=exp_data, index=idx) for idx, exp_data in
        #  enumerate(expenses_dict.get(UrlaXmlKeys.EXPENSE))],  ## <-- ERROR in _build_id_list()
        [Loan(data=loan_data, index=idx) for idx, loan_data in
         enumerate(loan_dict.get(UrlaXmlKeys.LOAN))],
        [Party(data=party_data, index=idx) for idx, party_data in
         enumerate(party_dict.get(UrlaXmlKeys.PARTY))],
        [Collateral(data=collat_data, index=idx) for idx, collat_data in
         enumerate(collat_dict.get(UrlaXmlKeys.COLLATERAL))],
    ]

    # Visually inspect the first element of each deal_list element
    target_index = 1
    for obj_list in deal_lists:
        for idx, obj in enumerate(obj_list):
            if idx == target_index - 1 and idx < len(obj_list):
                print(f"({idx}): {obj.type} [NAME = {obj.name}]\n"
                      f"\tPATH: {obj.xpath}\n"
                      f"\tID_SET: {obj.id_set}\n"
                      f"\tDATA: {pprint.pformat(obj.data)}\n")
        print()
