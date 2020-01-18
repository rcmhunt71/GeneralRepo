import os
import typing
from collections import OrderedDict

import xmltodict
from models.urla_xml_keys import UrlaXmlKeys, ElementPath


class UrlaXML:
    """

    This class reads and converts the MISMO v3.4 XML into a complex, nested python data structure. It removes the need
    to process the XML, and allows the user to quickly access the various data elements within the XML.

    """
    def __init__(self, source_file_name: str) -> typing.NoReturn:
        self.source_file_name = source_file_name
        self.data = self.convert_xml_to_dict(source_file_name)

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

    def get_assets(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the ASSETS level.
        :return: List of OrderedDicts containing the ASSET data.
        """
        family = UrlaXmlKeys.ASSETS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_liabilities(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the LIABILITIES level.
        :return: List of OrderedDicts containing the LIABILITY data.
        """
        family = UrlaXmlKeys.LIABILITIES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_loans(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the LOANS level.
        :return: List of OrderedDicts containing the LOAN data.
        """
        family = UrlaXmlKeys.LOANS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_collaterals(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the COLLATERALS level.
        :return: List of OrderedDicts containing the COLLATERAL data.
        """
        family = UrlaXmlKeys.COLLATERALS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_expenses(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the EXPENSES level.
        :return: List of OrderedDicts containing the EXPENSE data.
        """
        family = UrlaXmlKeys.EXPENSES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_relationships(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the RELATIONSHIPS level.
        :return: List of OrderedDicts containing the RELATIONSHIP data.
        """
        family = UrlaXmlKeys.RELATIONSHIPS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_parties(self) -> OrderedDict:
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

    def _get_element_family(self, family: str) -> OrderedDict:
        """
        Get the OrderedDict stored at the specified level.
        :return: List of OrderedDicts containing the specified data.
        """
        return self._get_nested_subdict(keys_list=getattr(ElementPath(), f"{family.upper()}_PATH"))
