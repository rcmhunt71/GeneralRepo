import argparse
import json
import os
import pprint
import typing

from models.singular_xml_models import Asset, Collateral, Liability, Loan, Party
from models.urla_xml_model import UrlaXML, UrlaXmlKeys


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


def write_debug_files(source_obj: UrlaXML, compare_obj: UrlaXML) -> typing.NoReturn:
    """
    Given the UrlaXML objs, write each objects's OrderedDict as a str (OrderedDict = output from converting XML to dict)

    :param source_obj: Source XML object
    :param compare_obj: Comparison XML object

    :return: None

    """
    # Outfile definition parameters
    outfile_dir, outfile_ext = ('outfiles', 'out')
    indent, width = (4, 180)

    # Build file spec (filename + path)
    out_primary_file_spec = _build_out_filename(
        target_dir=outfile_dir, input_fname=source_obj.source_file_name, ext=outfile_ext)
    out_compare_file_spec = _build_out_filename(
        target_dir=outfile_dir, input_fname=compare_obj.source_file_name, ext=outfile_ext)

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
    source = UrlaXML(source_file_name=cli.args.source)
    compare = UrlaXML(source_file_name=cli.args.compare)

    # Write debug files if requested
    if cli.args.outfile:
        write_debug_files(source_obj=source, compare_obj=compare)

    # Get lists of OrderedDicts for various elements in the source MISMO v.3.4 XML
    assets_dict = source.get_assets()
    liabilities_dict = source.get_liabilities()
    expenses_dict = source.get_expenses()
    loan_dict = source.get_loans()
    party_dict = source.get_parties()
    collat_dict = source.get_collaterals()

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
