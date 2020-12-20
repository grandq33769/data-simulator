# Standard Library
from typing import List

from ...model.data import Attribute, DataModel
from ...model.et.data import DRBidCEMS, ETBidSubmit
from ...model.et.env import ETAuthorization, ETConfig, ETEnvironment
from .shared import ENDPOINT

AUTH = ETAuthorization(account='sample', password='test')

ENV = ETEnvironment(
    auth=AUTH,
    endpoint=ENDPOINT,
)

DATA: List[DataModel] = [
    DRBidCEMS(
        scope='hour',
        frequency=['00:00'],
        callback=lambda *args: print('hello'),
        uuid=Attribute(get=lambda *args: ['a'], kwargs={}),
        start_time=Attribute(get=lambda *args: '2020-01-01 11', kwargs={}),
        end_time=Attribute(get=lambda *args: '2020-01-01 12', kwargs={}),
        quantity=3,
    ),
    ETBidSubmit(
        scope='day',
        frequency=['00:00'],
        callback=lambda: None,
        bid_type=Attribute(get=lambda *args: 'buy', kwargs={}),
        start_time=Attribute(get=lambda *args: '2020-01-01 11', kwargs={}),
        end_time=Attribute(get=lambda *args: '2020-01-01 12', kwargs={}),
        value=Attribute(get=lambda *args: '3', kwargs={}),
        price=Attribute(get=lambda *args: '5', kwargs={}),
    ),
]

CONFIG = ETConfig(ENV, DATA)
