import unittest
from random import randrange, choice

from PRICE.APIs.extra_data.models.extra_data import (ExtraDataEntryKeys, ExtraDataEntry,
                                                     ExtraDataEntryList, ExtraDataKeys,
                                                     ExtraDataMetadataEntryKeys, ExtraDataMetadataEntry,
                                                     ExtraDataMetadataEntryList, ExtraDataMetadataKeys)
from PRICE.APIs.extra_data.responses.extra_data import ExtraData
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

extra_data_model_data_names = ['Some ED Field', 'Another ED field', 'YAEF - Yet Another ED Field']
extra_data_model_data_values = ['Example', 'SomeEDField', 'AnotherExample', 'AnotherEDField']
metadata_data_types = ['Binary', "Text", "CSV", "Unknown"]

NUMBER_EXTRA_DATA_ENTRIES = 4


def build_extra_data_model_entry_data():
    return {
        ExtraDataEntryKeys.DATA_NAME: choice(extra_data_model_data_names),
        ExtraDataEntryKeys.DATA_VALUE: choice(extra_data_model_data_values),
        ExtraDataEntryKeys.DATA_NUMERIC_VALUE: randrange(10),
        ExtraDataEntryKeys.ROW_NUMBER_ID: randrange(1000),
    }


extra_data_model_entries = [build_extra_data_model_entry_data() for _ in range(NUMBER_EXTRA_DATA_ENTRIES)]


def build_extra_data_model_metadata_entry_data():
    return {
        ExtraDataMetadataEntryKeys.DATA_NAME: choice(extra_data_model_data_names),
        ExtraDataMetadataEntryKeys.DATA_VALUE: choice(extra_data_model_data_values),
        ExtraDataMetadataEntryKeys.EXTRA_DATA_TYPE: choice(metadata_data_types),
    }


extra_data_model_md_entries = [build_extra_data_model_metadata_entry_data() for _
                               in range(NUMBER_EXTRA_DATA_ENTRIES)]


class TestExtraData(unittest.TestCase, CommonResponseValidations):
    def test_extra_data_entry_model(self):
        extra_data_entry_args = build_extra_data_model_entry_data()
        extra_data_entry_model = ExtraDataEntry(**extra_data_entry_args)
        self._validate_response(model=extra_data_entry_model, model_data=extra_data_entry_args)

    def test_extra_data_entry_list(self):
        extra_data_entry_list_model = ExtraDataEntryList(*extra_data_model_entries)
        self._verify(descript=f"{extra_data_entry_list_model.model_name}: Verify correct number of elements",
                     actual=len(extra_data_entry_list_model), expected=len(extra_data_model_entries))

        for index, sub_model in enumerate(extra_data_entry_list_model):
            self._validate_response(model=sub_model, model_data=extra_data_model_entries[index])

    def test_extra_data_only_response(self):
        key = ExtraDataKeys.EXTRA_DATA
        extra_data_args = response_args.copy()
        extra_data_args[key] = extra_data_model_entries
        extra_data_response = ExtraData(**extra_data_args)

        self._verify(descript=f"{extra_data_response.model_name}: has correct attribute: {key}.",
                     actual=hasattr(extra_data_response, key), expected=True)

        self._validate_response(model=extra_data_response, model_data=extra_data_args)


class TestExtraMetadataData(unittest.TestCase, CommonResponseValidations):
    def test_extra_data_metadata_entry_model(self):
        extra_data_metadata_entry_args = build_extra_data_model_metadata_entry_data()
        extra_data_entry_model = ExtraDataMetadataEntry(**extra_data_metadata_entry_args)
        self._validate_response(model=extra_data_entry_model, model_data=extra_data_metadata_entry_args)

    def test_extra_data_entry_list(self):
        extra_data_md_entry_list_model = ExtraDataMetadataEntryList(*extra_data_model_md_entries)
        self._verify(descript=f"{extra_data_md_entry_list_model.model_name}: Verify correct number of elements.",
                     actual=len(extra_data_md_entry_list_model), expected=len(extra_data_model_md_entries))

        for index, sub_model in enumerate(extra_data_md_entry_list_model):
            self._validate_response(model=sub_model, model_data=extra_data_model_md_entries[index])

    def test_extra_data_metadata_only_response(self):
        key = ExtraDataMetadataKeys.EXTRA_DATA_METADATA
        extra_data_md_args = response_args.copy()
        extra_data_md_args[key] = extra_data_model_md_entries
        extra_data_md_response = ExtraData(**extra_data_md_args)

        self._verify(descript=f"{extra_data_md_response.model_name}: has correct attribute: {key}.",
                     actual=hasattr(extra_data_md_response, key), expected=True)

        self._validate_response(model=extra_data_md_response, model_data=extra_data_md_args)


class TestAllExtraDataMetadata(unittest.TestCase, CommonResponseValidations):
    def test_extra_data_and_extra_metadata_response(self):
        d_key = ExtraDataKeys.EXTRA_DATA
        md_key = ExtraDataMetadataKeys.EXTRA_DATA_METADATA
        extra_data_args = response_args.copy()
        extra_data_args[d_key] = extra_data_model_entries
        extra_data_args[md_key] = extra_data_model_md_entries

        extra_data_response = ExtraData(**extra_data_args)

        for key in [d_key, md_key]:
            self._verify(descript=f"{extra_data_response.model_name}: has correct attribute: {key}.",
                         actual=hasattr(extra_data_response, key), expected=True)

        self._validate_response(model=extra_data_response, model_data=extra_data_args)


if __name__ == '__main__':
    unittest.main()
