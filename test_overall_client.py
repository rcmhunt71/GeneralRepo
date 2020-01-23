import unittest

from APIs.client import Client
from logger.logging import Logger

log = Logger()

# ================================================================
#     Client Info
# ================================================================

specific_subclient_methods = {
    "loan": ['get_loan', 'import_from_file', 'get_loan_statuses', 'set_loan_data']
}

client_args = {
    "base_url": "auto.test.pclender.dom",
    'database': "testset1",
    'port': 8080,
    'headers': {"CONTENT_TYPE": "application/JSON"},
}


class TestGeneralAPIClient(unittest.TestCase):
    def test_general_api_client(self):
        client = Client(**client_args)

        for sub_client, api_calls in specific_subclient_methods.items():
            log.debug(f"Verify primary client has a secondary '{sub_client}' client.")
            self.assertEqual(hasattr(client, sub_client), True)
            target_client = getattr(client, sub_client)

            for client_attr_name, client_attr_value in client_args.items():
                log.debug(f"Verify secondary client '{sub_client}' has data element '{client_attr_name}' "
                          f"with value '{client_attr_value}'.")
                self.assertEqual(getattr(target_client, client_attr_name), client_attr_value)

            for api_call in api_calls:
                log.debug(f"Verify secondary client '{sub_client}' has an API method '{api_call}'.")
                self.assertEqual(hasattr(target_client, api_call), True)


if __name__ == '__main__':
    unittest.main()
