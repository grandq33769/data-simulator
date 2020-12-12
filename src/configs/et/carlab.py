# Standard Library
from typing import List

from ...model.et.data import DRBidCEMS, ETBidSubmit
from ...model.et.env import ETAuthorization, ETConfig, ETEnvironment
from ...model.model import Attribute, DataModel
from .shared import ENDPOINT

AUTH = ETAuthorization(account='Carlab_CEMS', password='test')

ENV = ETEnvironment(auth=AUTH, endpoint=ENDPOINT,)

DATA: List[DataModel] = [
    DRBidCEMS(
        scope='hour',
        frequency=['00:00'],
        callback=lambda: None,
        uuid=Attribute(get=lambda: ['a'], args={}),
        start_time=Attribute(get=lambda: '2020-01-01 11', args={}),
        end_time=Attribute(get=lambda: '2020-01-01 12', args={}),
    ),
    ETBidSubmit(
        scope='hour',
        frequency=['00:00'],
        callback=lambda: None,
        bid_type=Attribute(get=lambda: 'buy', args={}),
        start_time=Attribute(get=lambda: '2020-01-01 11', args={}),
        end_time=Attribute(get=lambda: '2020-01-01 12', args={}),
        value=Attribute(get=lambda: '3', args={}),
        price=Attribute(get=lambda: '5', args={}),
    ),
]

CONFIG = ETConfig(ENV, DATA)
