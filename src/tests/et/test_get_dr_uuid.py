from ...model.et.env import ETEnvironment
from ...simulate.et import get_dr_uuid


def test_get_dr_uuid(host, auth):
    kwargs = {
        'date_str': '2020-11-26',
        'env': ETEnvironment(auth=auth, endpoint=host),
    }
    result = get_dr_uuid(**kwargs)
    assert isinstance(result, list)
    for uuid in result:
        assert isinstance(uuid, str)
