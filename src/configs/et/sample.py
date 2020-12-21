# Standard Library
from typing import List

from ...callback.rest.request import http_request
from ...model.data import Attribute, Callback, DataModel
from ...model.et.data import DRBidCEMS, ETBidSubmit
from ...model.et.env import ETAuthorization, ETConfig, ETEnvironment
from ...simulate.et import get_dr_uuid
from ...simulate.math import get_float
from ...simulate.time import get_end_depend_start, get_hour_by_range
from .shared import ENDPOINT, LOGIN_CALLBACK, LOGIN_URL

AUTH = ETAuthorization(
    account='test',
    password='test',
    path=LOGIN_URL,
    callback=LOGIN_CALLBACK,
)

ENV = ETEnvironment(
    auth=AUTH,
    endpoint=ENDPOINT,
)

DATA: List[DataModel] = [
    DRBidCEMS(
        scope='day',
        frequency=['10:30'],
        callback=Callback(
            func=http_request, kwargs={'method': 'post', 'path': 'DR_bid'}
        ),
        uuid=Attribute(get=get_dr_uuid),
        start_time=Attribute(
            get=get_hour_by_range, kwargs={'start': 13, 'end': 14}
        ),
        end_time=Attribute(
            get=get_hour_by_range, kwargs={'start': 15, 'end': 17}
        ),
    ),
    ETBidSubmit(
        scope='day',
        frequency=['08:00'],
        callback=Callback(
            func=http_request, kwargs={'method': 'post', 'path': 'bidsubmit'}
        ),
        bid_type=Attribute(get=lambda **kwargs: 'sell'),
        start_time=Attribute(
            get=get_hour_by_range,
            kwargs={'start': 12, 'end': 16, 'dt_format': '%Y/%m/%d %H'},
        ),
        end_time=Attribute(
            get=get_end_depend_start, kwargs={'dt_format': '%Y/%m/%d %H'}
        ),
        value=Attribute(
            get=get_float, kwargs={'start': 5, 'end': 40, 'digit': 2}
        ),
        price=Attribute(
            get=get_float, kwargs={'start': 6, 'end': 12, 'digit': 1}
        ),
        quantity=30,
    ),
    ETBidSubmit(
        scope='day',
        frequency=['08:00'],
        callback=Callback(
            func=http_request, kwargs={'method': 'post', 'path': 'bidsubmit'}
        ),
        bid_type=Attribute(get=lambda **kwargs: 'buy'),
        start_time=Attribute(
            get=get_hour_by_range,
            kwargs={'start': 14, 'end': 16, 'dt_format': '%Y/%m/%d %H'},
        ),
        end_time=Attribute(
            get=get_end_depend_start, kwargs={'dt_format': '%Y/%m/%d %H'}
        ),
        value=Attribute(
            get=get_float, kwargs={'start': 3, 'end': 10, 'digit': 2}
        ),
        price=Attribute(
            get=get_float, kwargs={'start': 10, 'end': 12, 'digit': 1}
        ),
        quantity=10,
    ),
]

CONFIG = ETConfig(ENV, DATA)
