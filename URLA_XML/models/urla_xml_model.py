import os
import typing
from collections import OrderedDict

import xmltodict
from models.singular_xml_models import Asset, Liability, Expense, Loan, Party, Collateral
from models.urla_xml_keys import UrlaXmlKeys, ElementPath


class UrlaXML:
    """

    This class reads and converts the MISMO v3.4 XML into a complex, nested python data structure. It removes the need
    to process the XML, and allows the user to quickly access the various data elements within the XML.

    """
    def __init__(self, source_file_name: str, primary_source: bool = False) -> typing.NoReturn:
        self.source_file_name = source_file_name
        self.primary_source = primary_source
        self.data = self.convert_xml_to_dict(source_file_name)

    def read_file(self, filename: str) -> typing.List[str]:
        file_type = "primary" if self.primary_source else "comparison"
        print(f"Reading {file_type} file: '{os.path.abspath(filename)}'")
        with open(filename, "r") as FILE:
            return FILE.readlines()

    def convert_xml_to_dict(self, file_spec: str) -> OrderedDict:
        """
        Reads XML and converts the contents to a nested collections.OrderedDict
        :param file_spec: filespec of the input XML file.

        :return: OrderedDict representation of the XML.

        """
        if not os.path.exists(file_spec):
            raise FileNotFoundError(f"XML Source file ('{file_spec}') was not found.")

        file_contents = self.read_file(file_spec)
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
                # print(f"\tFound key: {key} --> Key Sequence: {keys_list} --> Next set of keys: {data_subset.keys()}")
            else:
                print(f"\tNOTE: Key not found: {key} --> Requested Key Sequence: {keys_list}")
                break

        return data_subset

    def get_assets_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the ASSETS level.
        :return: List of OrderedDicts containing the ASSET data.
        """
        family = UrlaXmlKeys.ASSETS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_assets_elements(self) -> typing.List[Asset]:
        """
        Get the list of elements stored in the OrderedDict at the ASSETS level.
        :return: List of OrderedDicts containing the ASSET data.
        """
        family = UrlaXmlKeys.ASSETS
        child = UrlaXmlKeys.ASSET
        model = Asset
        return self._get_elements(family=family, child=child, model=model)

    def get_liabilities_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the LIABILITIES level.
        :return: List of OrderedDicts containing the LIABILITY data.
        """
        family = UrlaXmlKeys.LIABILITIES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_liabilities_elements(self) -> typing.List[Liability]:
        """
        Get the list of elements stored in the OrderedDict at the LIABILITIES level.
        :return: List of OrderedDicts containing the LIABILITY data.
        """
        family = UrlaXmlKeys.LIABILITIES
        child = UrlaXmlKeys.LIABILITY
        model = Liability
        return self._get_elements(family=family, child=child, model=model)

    def get_loans_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the LOANS level.
        :return: List of OrderedDicts containing the LOAN data.
        """
        family = UrlaXmlKeys.LOANS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_loans_elements(self) -> typing.List[Loan]:
        """
        Get the list of elements stored in the OrderedDict at the LOANS level.
        :return: List of OrderedDicts containing the LOAN data.
        """
        family = UrlaXmlKeys.LOANS
        child = UrlaXmlKeys.LOAN
        model = Loan
        return self._get_elements(family=family, child=child, model=model)

    def get_collaterals_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the COLLATERALS level.
        :return: List of OrderedDicts containing the COLLATERAL data.
        """
        family = UrlaXmlKeys.COLLATERALS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_collaterals_elements(self) -> typing.List[Collateral]:
        """
        Get the list of elements stored in the OrderedDict at the COLLATERALS level.
        :return: List of OrderedDicts containing the COLLATERAL data.
        """
        family = UrlaXmlKeys.COLLATERALS
        child = UrlaXmlKeys.COLLATERAL
        model = Collateral
        return self._get_elements(family=family, child=child, model=model)

    def get_expenses_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the EXPENSES level.
        :return: List of OrderedDicts containing the EXPENSE data.
        """
        family = UrlaXmlKeys.EXPENSES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_expenses_elements(self) -> typing.List[Expense]:
        """
        Get the list of elements stored in the OrderedDict at the EXPENSES level.
        :return: List of OrderedDicts containing the EXPENSE data.
        """
        family = UrlaXmlKeys.EXPENSES
        child = UrlaXmlKeys.EXPENSE
        model = Expense
        return self._get_elements(family=family, child=child, model=model)

    def get_relationships_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the RELATIONSHIPS level.
        :return: List of OrderedDicts containing the RELATIONSHIP data.
        """
        family = UrlaXmlKeys.RELATIONSHIPS
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_parties_dict(self) -> OrderedDict:
        """
        Get the OrderedDict stored at the PARTIES level.
        :return: List of OrderedDicts containing the PARTY data.
        """
        family = UrlaXmlKeys.PARTIES
        return self._check_value_is_list(self._get_element_family(family=family))

    def get_parties_elements(self) -> typing.List[Party]:
        """
        Get the list of elements stored in the OrderedDict at the PARTIES level.
        :return: List of OrderedDicts containing the PARTY data.
        """
        family = UrlaXmlKeys.PARTIES
        child = UrlaXmlKeys.PARTY
        model = Party
        return self._get_elements(family=family, child=child, model=model)

    def _get_elements(self, family: str, child: str, model) -> typing.List:
        """
        Get the list of singular elements from the family/parent (plural tag)
        :param family: Plural tag (e.g. - ASSETS)
        :param child: Singular tag (e.g. - ASSET)
        :param model: Model to serialize each child into. (e.g. Asset)

        :return: List of instantiated/populated models of type 'model'
        """
        values = self._check_value_is_list(self._get_element_family(family=family)).get(child)
        return [model(data=asset_data, index=idx) for idx, asset_data in enumerate(values)]

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

        NOTE: 'family' is used to determine which value from ElementPath to get: e.g. - ElementsPath.ASSETS_PATH
        """
        return self._get_nested_subdict(keys_list=getattr(ElementPath(), f"{family.upper()}_PATH"))
