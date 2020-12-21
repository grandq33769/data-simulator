# Standard Library
import os
from urllib.parse import urlparse

from ...model.data import Callback

ENDPOINT = urlparse(os.environ.get('ET_HOST', 'http://localhost:5000'))
LOGIN_URL = '/login'
LOGIN_CALLBACK = Callback(func=lambda response: response['bearer'])
