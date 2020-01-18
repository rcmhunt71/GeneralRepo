import typing
from collections import OrderedDict

from models.urla_xml_keys import UrlaXmlKeys


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
