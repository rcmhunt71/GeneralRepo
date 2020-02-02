import typing
from collections import namedtuple

import prettytable
from comparator.comparison_engine import ComparisonEngine
from logger.logging import Logger

log = Logger()


class ComparisonReport:

    SOURCE = 'Source'
    EXACT = "Exact Match"
    CLOSEST = "Closest Match"
    NO_ENTRY = '--'
    ATTRIBUTE = "Attribute"
    PATH = "Path"
    XPATH = "XPath"
    SOURCE_VALUE = "Source Value"
    COMP_VALUE = "Comparison Value"
    DIFFERENCES = "ELEMENT DIFFERENCES"
    COMPARISON = 'Comparison'
    DIFFERENCE = "Diff?"
    DIFF_VALUE = "X"
    LEFT = 'l'
    CENTER = 'c'
    RIGHT = 'r'
    EMPTY = ''
    TAG = 'Tag'

    COLUMN = namedtuple('column', field_names=("name", "alignment"))

    def __init__(self, src_model, cmp_model, results=None):
        self.src_model = src_model
        self.cmp_model = cmp_model
        self.results = results

    def symmetrical_differences(self) -> str:
        """
        Create a report of symmetrical ELEMENT (not attribute) differences between the data sets.
        (Symmetrical = found in one dataset, but not the other, irrespective if source or comparison)

        :return: String representation of tabular results

        """
        diff = set(list(self.src_model.path_dict)) ^ set(list(self.cmp_model.path_dict))
        report = f"{self.DIFFERENCES}:"
        table = prettytable.PrettyTable()

        # Column name, order, and alignment
        setup = [self.COLUMN(self.SOURCE, self.CENTER),
                 self.COLUMN(self.TAG, self.CENTER),
                 self.COLUMN(self.PATH, self.LEFT)]

        table.field_names = [col.name for col in setup]
        for col in setup:
            table.align[col.name] = col.alignment

        for elem in sorted(diff):
            if elem in self.src_model.path_dict:
                row = [self.SOURCE.upper(), elem, '//' + '/'.join(self.src_model.path_dict[elem])]
            else:
                row = [self.COMPARISON.upper(), elem, '//' + '/'.join(self.cmp_model.path_dict[elem])]
            table.add_row(row)
        return f"{report}\n{table.get_string()}"

    def comparison_summary(self, title: str, results=None) -> str:
        """
        Builds table of overall results (perfect and closest matches)
        :param title: Title to prefix the table
        :param results: Results dictionary (defined in ComparisonEngine)
        :return: String representation of tabular results

        """
        results = results or self.results
        table = prettytable.PrettyTable()

        # Column name, order, and alignment
        setup = [self.COLUMN(self.SOURCE, self.LEFT),
                 self.COLUMN(self.EXACT, self.LEFT),
                 self.COLUMN(self.CLOSEST, self.LEFT)]
        table.field_names = [x.name for x in setup]
        for col in setup:
            table.align[col.name] = col.alignment

        if isinstance(results, dict):
            for xpath, data in results.items():
                exact_match = self.NO_ENTRY
                closest_match = ''

                if data[ComparisonEngine.MATCH] is not None:
                    exact_match = data[ComparisonEngine.MATCH].xpath_str
                else:
                    closest_match = None
                    if data[ComparisonEngine.CLOSEST_OBJ] is not None:
                        closest_match = (f"{data[ComparisonEngine.CLOSEST_OBJ].xpath_str} "
                                         f"({data[ComparisonEngine.CLOSEST_MATCH_COUNT]}/{data[ComparisonEngine.TOTAL]}"
                                         f" matches)")

                table.add_row([xpath, exact_match, closest_match])

        return f"{title}\n{table.get_string()}"

    def closest_match_info(self, results: typing.Dict[str, dict] = None) -> str:
        """
        Generates element-by-element comparison of closest match to source element.
        :param results: Results Data dictionary (defined by comparison_engine._compare_element_lists())
        :return: String representation of tabular results

        """
        title = 'Closest Match Report'

        # Column name, order, and alignment
        columns = [
            self.COLUMN(self.SOURCE, self.LEFT),
            self.COLUMN(self.CLOSEST, self.LEFT),
            self.COLUMN(self.ATTRIBUTE, self.LEFT),
            self.COLUMN(self.DIFFERENCE, self.CENTER),
            self.COLUMN(self.SOURCE_VALUE, self.LEFT),
            self.COLUMN(self.COMP_VALUE, self.LEFT),
        ]

        table = prettytable.PrettyTable()
        table.field_names = [col.name for col in columns]
        for col in columns:
            table.align[col.name] = col.alignment

        results = results or self.results
        if results is not None:
            for xpath, data in results.items():
                if data[ComparisonEngine.CLOSEST_MATCH_COUNT] <= 0:
                    continue

                diff = self._build_differences(xpath, data)
                for src_xpath, src_data in diff.items():
                    for dst_xpath, dst_data in src_data.items():
                        table.add_row([src_xpath, dst_xpath, "", "", "", ""])

                        # Sort by the XPATH value (which is the value[self.XPATH] of dict.items() key/value tuple)
                        for index, (attr, attr_data) in enumerate(
                                sorted(dst_data.items(), key=lambda key_value_tuple: key_value_tuple[1][self.XPATH])):

                            row = ["", attr_data[self.XPATH], attr]

                            src_value = (self.NO_ENTRY if attr_data[self.SOURCE_VALUE] == "" else
                                         attr_data[self.SOURCE_VALUE])
                            cmp_value = (self.NO_ENTRY if attr_data[self.COMP_VALUE] == "" else
                                         attr_data[self.COMP_VALUE])
                            row.append(self.DIFF_VALUE if src_value != cmp_value else "")
                            row.append(src_value)
                            row.append(cmp_value)
                            table.add_row(row)

                    # After each comparison, add a blank line
                    table.add_row(["" for _ in range(len(columns))])

        return f"{title}\n{table.get_string()}"

    def _build_differences(self, src_xpath: str, data: typing.Dict[str, typing.Any]) -> typing.Dict[str, dict]:
        """
        Builds a dictionary of element data matching/storage (src_xpath, cmp_xpath, attribute, src_value, cmp_value)
        :param src_xpath: Path to start comparison
        :param data: Results data dictionary (see ComparisonEngine._compare_element_lists())
        :return: Dictionary of element data matching/storage

        """
        # Add element name to XPATH if available (xpath index 3 may have a name of ELEMENT_4)
        if data[ComparisonEngine.SRC_OBJ].name != data[ComparisonEngine.SRC_OBJ].VALUE_NOT_SET:
            src_xpath += f" (NAME: {data[ComparisonEngine.SRC_OBJ].name})"

        # Data dictionary
        diff_dict = {src_xpath: {}}

        # Get the two nodes to compare
        src = data[ComparisonEngine.SRC_OBJ]
        cmp = data[ComparisonEngine.CLOSEST_OBJ]

        # Get children of the nodes
        src_children = ComparisonEngine.get_leaf_nodes(src)
        cmp_children = ComparisonEngine.get_leaf_nodes(cmp)

        # Convert child data to sets for easy comparison
        src_child_set = set([x.obj_path_str for x in src_children])
        cmp_child_set = set([x.obj_path_str for x in cmp_children])

        # For all element identified...
        for attr_found in sorted(src_child_set.union(cmp_child_set)):

            # Spilt obj_path based on OBJ_PATH_DELIMITER: '|' --> traversal_path | attributes
            attr_xpath = attr_found.split(src.OBJ_PATH_DELIMITER)[0]
            for attr_num, entry in enumerate(attr_found.split(src.OBJ_PATH_DELIMITER)[1:]):

                # Add cmp_xpath if not defined
                cmp_xpath = data[ComparisonEngine.CLOSEST_OBJ].xpath_str
                if data[ComparisonEngine.CLOSEST_OBJ].name != data[ComparisonEngine.CLOSEST_OBJ].VALUE_NOT_SET:
                    cmp_xpath += f" (NAME: {data[ComparisonEngine.CLOSEST_OBJ].name})"

                if cmp_xpath not in diff_dict[src_xpath]:
                    diff_dict[src_xpath][cmp_xpath] = {}

                # Split node attributes by ENTRY_DELIMITER: ':'
                cmp_attr_data = entry.split(src.ENTRY_DELIMITER)

                # If new attribute, add to dict[src_xpath][cmp_xpath][new_attr] = {}
                attr_name = cmp_attr_data[0]
                if attr_name not in diff_dict[src_xpath][cmp_xpath]:
                    diff_dict[src_xpath][cmp_xpath][attr_name] = {
                        self.XPATH: attr_xpath,
                        self.SOURCE_VALUE: self.NO_ENTRY,
                        self.COMP_VALUE: self.NO_ENTRY}

                # If the current attribute difference is in the src
                if attr_found in src_child_set:
                    diff_dict[src_xpath][cmp_xpath][attr_name][
                        self.SOURCE_VALUE] = src.ENTRY_DELIMITER.join(cmp_attr_data[1:])

                # Else if the current attribute difference is in the cmp
                if attr_found in cmp_child_set:
                    diff_dict[src_xpath][cmp_xpath][attr_name][
                        self.COMP_VALUE] = src.ENTRY_DELIMITER.join(cmp_attr_data[1:])

        return diff_dict
