# Mock of requests until able install Requests
class MockRequests:

    @classmethod
    def get(cls, url, params=None, headers=None):
        return Response(url=url, params=params, method='get', headers=headers)

    @classmethod
    def post(cls, url, data, params=None, headers=None):
        return Response(url=url, method='post', params=params, data=data, headers=headers)

    @classmethod
    def delete(cls, url, params=None, headers=None):
        return Response(url=url, method='delete', params=params, headers=headers)

    @classmethod
    def put(cls, url, data, params=None, headers=None):
        return Response(url=url, method='put', params=params, data=data, headers=headers)


class Response:
    def __init__(self, url, method, params=None, data=None, headers=None):
        self.raw = "RAW CONTENT"
        self.content = "CONTENT"
        self.headers = headers or {}
        self.params = params or {}
        self.payload = data or {}
        self.url = url
        self.method = method
        self.encoding = "ISO-8859-1"
        self.text = [attr for attr in dir(self) if not attr.startswith('__')]
