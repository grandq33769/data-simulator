# Standard Library
from datetime import datetime, timedelta
from random import randrange, sample
from typing import List, Optional, Sequence

from ..callback.rest.request import http_request
from ..model.et.env import ETEnvironment


def get_dr_uuid(**kwargs) -> List[str]:
    env: Optional[ETEnvironment] = kwargs.get('env')
    date_str: Optional[str] = kwargs.get('date_str')
    result: Sequence[dict] = []

    if date_str is None:
        tomorrow = datetime.now() + timedelta(days=1)
        date_str = tomorrow.strftime('%Y-%m-%d')
    kwargs = {
        'data': {'date': date_str},
        'path': 'DR_bid',
        'method': 'get',
        'env': env,
    }
    res = http_request(**kwargs)
    bids: Sequence[dict] = [*res]

    try:
        quantity = randrange(len(bids))
        result = sample(bids, quantity)
    except ValueError:
        pass
    except TypeError:
        pass

    return [bid['uuid'] for bid in result]
