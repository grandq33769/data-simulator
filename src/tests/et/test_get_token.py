from ...callback.rest.request import get_token
from ...model.config import Environment


def test_get_token(host, auth):
    kwargs = {
        'auth': auth,
        'env': Environment(endpoint=host),
    }
    result = get_token(**kwargs)
    assert isinstance(result, dict)
    assert 'Authorization' in result
    assert len(result.get('Authorization')) == 249
