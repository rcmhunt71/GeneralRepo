import typing

from models.singular_xml_element_base_model import BaseDealElement
from models.urla_xml_model import UrlaXML


class DataMatch:
    """ Simple data tracking class for mapping source entry to matching comparison entry """
    def __init__(self, id_set, source_obj: BaseDealElement, found=False,
                 match_obj: BaseDealElement = None) -> typing.NoReturn:
        """

        :param id_set: XPATH set and value (':' delimited)
        :param source_obj: Source Inherited BaseDealElement
        :param found: (bool) True = match found
        :param match_obj: If match is True, the corresponding Comparison BaseDealElement

        """
        self.id_set = id_set
        self.source_obj = source_obj
        self.found = found
        self.match_obj = match_obj


class ComparisonEngine:
    def __init__(self, primary: UrlaXML, comparison: UrlaXML):
        self.primary = primary
        self.comparison = comparison

    def compare_and_map_singular_elements(self, element_name: str, details: bool = False) -> typing.List[DataMatch]:
        """
        Compare su
        :param element_name: name of URDA element to compare (should be plural, so all singular elements are compared
        :param details: (boolean) - If True, generate a summary report

        :return: List of DataMatch objects with corresponding matches (or unmatched)
        """
        # Verify requested Deal Type is plural (ends in 's') and is a recognized model.
        if (not hasattr(self.primary, f"get_{element_name.lower()}_elements") or
                not element_name.lower().endswith('s')):
            print(f"**ERROR**: Unrecognized Plural Deal Type: {element_name.lower()}.")
            return []

        # Get list of singular DealElements (type specified via parameters)
        source_data_elem = getattr(self.primary, f"get_{element_name.lower()}_elements")()
        comp_data_elem = getattr(self.comparison, f"get_{element_name.lower()}_elements")()

        # Build list of tuples to track mappings
        source_data = [DataMatch(id_set=elem.id_set, found=False, source_obj=elem, match_obj=None) for elem
                       in source_data_elem]
        comp_data = [DataMatch(id_set=elem.id_set, found=False, source_obj=elem, match_obj=None) for elem
                     in comp_data_elem]

        # Iterate through src doc looking for matches in the comparison doc
        matches = 0
        for src_elem in source_data:
            for comp_elem in comp_data:

                # If comparison element has a match, don't do the comparison
                if comp_elem.found:
                    continue

                # If the SRC is identical or is a superset of the comparison, associate the elements.
                if src_elem.id_set >= comp_elem.id_set:
                    matches += 1

                    src_elem.found = True
                    src_elem.match_obj = comp_elem.source_obj

                    comp_elem.found = True
                    comp_elem.match_obj = src_elem.source_obj

                    if details:
                        print(f"MATCH FOUND for {element_name}:\n   SRC:\n"
                              f"   {src_elem.id_set} ({src_elem.source_obj.seq_num})")
                        print(f"   COMP:\n   {src_elem.match_obj.id_set} ({src_elem.match_obj.seq_num})\n")

        print(f"SUMMARY FOR '{element_name}': {matches} matches.")

        return source_data

    def build_results_table(self, results):
        pass
