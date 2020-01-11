from enum import Enum
from base.mocks.mock_requests import MockRequests as requests


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
        self.URL = f"{self.base_url}/{database}"
        self.headers = headers or {}

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

    def _make_call(self, resource_endpoint, response_model, method, data=None, headers=None, params=None):
        params = params or {}
        data = data or {}
        headers = headers or self.headers
        url = f"{self.URL}/{resource_endpoint}"

        args = {'url': url, 'params': params, 'headers': headers}
        if method in [Methods.POST, Methods.PUT]:
            args['data'] = data

        response = getattr(requests, method.lower())(**args)
        model = response_model(response.content)
        model.response = response
        return model
