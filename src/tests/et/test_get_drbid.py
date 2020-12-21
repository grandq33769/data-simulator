from ...callback.rest.request import http_request
from ...model.et.env import ETEnvironment


def test_get_drbid(host, auth):
    kwargs = {
        'data': {'date': '2020-11-26'},
        'path': 'DR_bid',
        'method': 'get',
        'env': ETEnvironment(auth=auth, endpoint=host),
    }
    result = http_request(**kwargs)
    assert isinstance(result, list)
