# Standard Library
import os

# Third Party Library
import pytest

from ...model.config import Callback
from ...model.et.env import ETAuthorization


@pytest.fixture(scope="module")
def host():
    return 'https://et.udc-service.io:5000'


@pytest.fixture(scope="module")
def auth():
    return ETAuthorization(
        account=os.environ.get('ET_TEST_AC'),
        password=os.environ.get('ET_TEST_PW'),
        path='/login',
        callback=Callback(func=lambda response: response['bearer']),
    )
