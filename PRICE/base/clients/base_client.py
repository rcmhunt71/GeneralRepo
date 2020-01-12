from enum import Enum
from PRICE.base.mocks.mock_requests import MockRequests as requests
from PRICE.logger.logging import Logger

log = Logger()


class Methods(Enum):
    GET = 'get'
    PUT = 'put'
    POST = 'post'
    DELETE = 'delete'
    HEAD = 'head'
    OPTIONS = 'options'


class BaseClient:
    def __init__(self, base_url, database, port=None, headers=None):
        self.base_url = f"{base_url}:{port}" if port is not None else base_url
        self.url = f"{self.base_url}/{database}"
        self.headers = headers or {}
        self.test_response_data = None

        if not self.url.lower().startswith("http"):
            self.url = f"https://{self.url}"

    def insert_test_response_data(self, data):
        self.test_response_data = data

    def get(self, resource_endpoint, response_model, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model,
                               method=Methods.GET, headers=headers, params=params)

    def delete(self, resource_endpoint, response_model, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model,
                               method=Methods.DELETE, headers=headers, params=params)

    def post(self, resource_endpoint, response_model, data, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model, data=data,
                               method=Methods.POST, headers=headers, params=params)

    def put(self, resource_endpoint, data, response_model, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model, data=data,
                               method=Methods.PUT, headers=headers, params=params)

    def _make_call(self, resource_endpoint, response_model_class, method, data=None, headers=None, params=None):
        params = params or {}
        data = data or {}
        headers = headers or self.headers
        url = f"{self.url}/{resource_endpoint}"
        args = {'url': url, 'params': params, 'headers': headers}

        log.debug(f"URL: {method.value.upper()} {self.url}")
        log.debug(f"PARAMS: {params}")
        log.debug(f"HEADERS: {headers}")

        if method in [Methods.POST, Methods.PUT]:
            args['data'] = data

        full_url_request = f"{method.value.upper()} {url}"
        if params:
            full_url_request += f"?{params}"
        log.debug(f"Making call to: {full_url_request}")
        response = getattr(requests, method.value.lower())(**args)

        # TEST: Insert test response data in call response
        response_type = "RESPONSE"
        if self.test_response_data is not None:
            response.content = self.test_response_data
            response_type = "TEST RESPONSE"
        log.debug(f"{response_type}: {response.content}")

        response_model = response_model_class(**response.content)
        log.debug(f"Response Model: {type(response_model)}")

        response_model.response = response
        return response_model
