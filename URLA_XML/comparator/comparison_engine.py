import typing

from logger import logging
from models.element_base_model import BaseElement
from models.urla_xml_model import UrlaXML

log = logging.Logger()


class ComparisonEngine:
    MATCH = "Match"
    CLOSEST_MATCH_COUNT = "ClosestMatchCount"
    CLOSEST_OBJ = "ClosestObj"
    SRC_OBJ = 'SrcObj'
    CMP_OBJ = 'CmpObj'
    TOTAL = 'Total'
    HEADER_LENGTH = 120

    def __init__(self, primary: UrlaXML, comparison: UrlaXML) -> typing.NoReturn:
        self.primary = primary
        self.comparison = comparison

    def compare(self, element_name: str) -> typing.Dict[str, dict]:
        """

        :param element_name:
        :return:
        """
        if element_name not in self.primary.model.path_dict.keys():
            log.error(f"ERROR: Element '{element_name}' not found in the primary model. Available elements:")
            log.error(sorted(list(self.primary.model.path_dict.keys())))
            return {}

        for line in self._build_log_header(f"Comparing element: '{element_name}'"):
            log.info(line)

        # Get the target nodes from each XML file
        log.debug(f"Getting SRC NODES")
        src_nodes = self.get_elements(element_name=element_name, root=self.primary.model)

        log.debug(f"Getting CMP NODES")
        cmp_nodes = self.get_elements(element_name=element_name, root=self.comparison.model)

        return self._compare_element_lists(source_list=src_nodes, compare_list=cmp_nodes)

    def _compare_element_lists(self, source_list: typing.List[BaseElement],
                               compare_list: typing.List[BaseElement]) -> typing.Dict[str, dict]:
        """
        Given two nodes (one from each source), comnpare the node attributes and children to find the matches and
        provide closest matches.

        :param source_list: List of nodes to compare and verify
        :param compare_list: List of nodes to compare (source of truth)

        :return: dictionary of: key=src node xpaths, value={dict of source data, match data, and nearest match)

        """
        log.debug(f"SRC NODES: {[x.xpath_str for x in source_list]}")
        log.debug(f"CMP NODES: {[x.xpath_str for x in compare_list]}")

        # Define the result tracking structure (for each element with the target tag)
        # Key: The XPATH for each target
        # Values: SRC = complete source structure underneath the target
        #         MATCH: Matching Node
        #
        results_dict = dict(
            [(src.xpath_str, {self.SRC_OBJ: src,
                              self.MATCH: None,
                              self.CLOSEST_MATCH_COUNT: 0,
                              self.TOTAL: 0,
                              self.CLOSEST_OBJ: None}) for src in source_list])
        cmp_match_found = []

        for src_node in source_list:
            log.debug(f"SOURCE NODE XPATH: {src_node.xpath_str}")

            for cmp_node in compare_list:
                log.debug(f"COMPARISON NODE XPATH: {cmp_node.xpath_str}")

                # Don't compare if match has been found
                if cmp_node.xpath_str in cmp_match_found:
                    log.debug(f"COMPARISON NODE ({cmp_node.xpath_str}) ALREADY MATCHED")
                    continue

                # If the src node matches current cmp node, then compare elements (including children)
                if self._compare_node(src_node=src_node, cmp_node=cmp_node):
                    log.debug(f"CMP node matches (attr + #_child): {cmp_node.xpath_str} "
                              f"-> Checking descendants...")
                    src_children = self.get_leaf_nodes(src_node)
                    cmp_children = self.get_leaf_nodes(cmp_node)

                    src_child_set = set([x.obj_path_str for x in src_children])
                    cmp_child_set = set([x.obj_path_str for x in cmp_children])

                    if src_child_set == cmp_child_set:
                        log.debug(f"**MATCH**: {src_node.xpath_str} and {cmp_node.xpath_str}")
                        results_dict[src_node.xpath_str][self.MATCH] = cmp_node
                        results_dict[src_node.xpath_str][self.CLOSEST_OBJ] = cmp_node
                        results_dict[src_node.xpath_str][self.CLOSEST_MATCH_COUNT] = -1
                        cmp_match_found.append(cmp_node.xpath_str)
                        break
                    else:
                        distance = len(src_child_set.intersection(cmp_child_set))
                        if distance > results_dict[src_node.xpath_str][self.CLOSEST_MATCH_COUNT]:
                            results_dict[src_node.xpath_str][self.CLOSEST_MATCH_COUNT] = distance
                            results_dict[src_node.xpath_str][self.CLOSEST_OBJ] = cmp_node
                            results_dict[src_node.xpath_str][self.TOTAL] = len(src_child_set)

                        log.debug(f"DID NOT MATCH: {src_node.xpath_str} and {cmp_node.xpath_str}")
                        matches = src_child_set.intersection(cmp_child_set)
                        s_differences = src_child_set.symmetric_difference(cmp_child_set)
                        for match in matches:
                            log.debug(f"MATCHED: {match}")

                        for miss in sorted(s_differences):
                            target = "SRC" if miss in src_child_set else "CMP"
                            log.debug(f"{target}: {miss}")
                    log.debug("")

                else:
                    log.debug("SRC node and CMP node did not match (attributes and number of children)")
                    log.debug("")

        self._debug_print_results(results_dict)
        return results_dict

    @classmethod
    def get_leaf_nodes(cls, node: BaseElement) -> typing.List[BaseElement]:
        """
        Gets all leaf nodes below the provided root node. (Leaf = node without children)
        :param node: Specific node to use to start checking for leaf nodes (self + descendants)
        :return: List of leaf nodes (List of BaseElements)

        """
        leaves = []
        if not node.children:
            leaves.append(node)
        else:
            for child in node.children:
                leaves.extend(cls.get_leaf_nodes(node=child))
        return leaves

    # -------------------------------------------------------------------------------------
    @staticmethod
    def _compare_node(src_node: BaseElement, cmp_node: BaseElement) -> bool:
        """
        Compare the attributes and the number of children. If they match, the nodes are considered equal.

        :param src_node: Source Node
        :param cmp_node: Comparisan Node

        :return: Bool: True = nodes match.
        """
        # Check if attributes (data) match and number/type of children
        attrs = sorted(src_node.attributes) == sorted(cmp_node.attributes)
        child_types = (sorted([child.type for child in src_node.children]) ==
                       sorted([child.type for child in cmp_node.children]))

        return attrs & child_types

    def get_elements(self, element_name: str, root: BaseElement) -> typing.List[BaseElement]:
        """
        Get the child elements of the element_name using the relative "root" node

        :param element_name: Name of element tag to to find
        :param root: relative starting node

        :return: List of nodes underneath the relative root

        """

        # Get the XPATH that corresponds to the element name
        paths = root.path_dict[element_name]

        log.debug(f"List of XPath(s) to '{element_name}': {paths}")

        results = []
        for path in paths:
            results.extend(self._get_elements(path=path.split(root.XPATH_DELIMITER), starting_node=root))
        log.debug(f"RESULTS: {[x.xpath_str for x in results]}")
        return results

    def _get_elements(self, path: typing.List[str], starting_node: BaseElement) -> typing.List[BaseElement]:
        """
        Get the element(s) under the specified path
        :param path: List of node types required to create the path to the target node.
        :param starting_node: Node used to start the retrieval process

        :return: List of Elements

        """
        results = []
        current_type = path[0]
        extra_debugging = False

        if extra_debugging:
            log.debug(f"Rec'd Path: {path}")
            log.debug(f"Rec'd Starting Node: {starting_node.type} --> '{starting_node.name}'")
            log.debug(f"Current Type to look for: {current_type}\n")

        matching_child_nodes = starting_node.get_children_by_type(child_type=current_type)

        # If the current node type matches the desired type and there are no more nodes in the path, return the node
        if matching_child_nodes:
            if len(path) == 1:

                log.debug(f"Node type ({starting_node.type}) has children of current type ({current_type}) "
                          f"and path has single element ({path}).\nReturning matching child nodes: "
                          f"{[x.xpath_str for x in matching_child_nodes]}\n")

                return matching_child_nodes

            new_path = path[1:]                      # Advance to the next step
            for child_node in matching_child_nodes:  # Next set of nodes to evaluate
                results.extend(self._get_elements(path=new_path, starting_node=child_node))

        return results

    def _debug_print_results(self, results_dict: typing.Dict[str, dict]) -> typing.NoReturn:
        """
        Quick and easy display of result output
        :param results_dict: results dictionary

        :return: None

        """
        for xpath, data in results_dict.items():
            debug_msg = f"XPATH: {xpath} --> "
            if data[self.MATCH] is not None:
                debug_msg += f"{data[self.MATCH].xpath_str}"
            else:
                debug_msg += "None"
                if data[self.CLOSEST_OBJ] is not None:
                    debug_msg += (f"--> Closest Match: {data[self.CLOSEST_OBJ].xpath_str} with "
                                  f"{data[self.CLOSEST_MATCH_COUNT]} descendant(s) matching.")
            log.debug(debug_msg)

    def _build_log_header(self, tag):
        border = "=" * self.HEADER_LENGTH

        header = "{{tag:^{entry_length}}}".format(entry_length=self.HEADER_LENGTH)
        header = header.format(tag=tag)
        return [f"+{border}+",
                f"|{header}|",
                f"+{border}+"]
