# Standard Library
import os

from ...model.data import Callback

ENDPOINT = os.environ.get('ET_HOST', 'http://localhost:5000')
LOGIN_URL = '/login'
LOGIN_CALLBACK = Callback(func=lambda response: response['bearer'])
