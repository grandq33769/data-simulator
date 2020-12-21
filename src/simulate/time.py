# Standard Library
from datetime import datetime, timedelta
from random import randrange

# Third Party Library
from dateutil import parser

FORMAT = '%Y-%m-%d %H:%M:%S'


def get_hour_by_freq(
    offset: int = 0, dt_format: str = FORMAT, **kwargs
) -> str:
    hour: int = 0
    time = kwargs.get('time')
    if isinstance(time, int):
        hour = time % 24

    today = datetime.now()
    today = today.replace(hour=hour, minute=0, second=0, microsecond=0)
    today = today + timedelta(hours=offset)
    return today.strftime(dt_format)


# pylint: disable=unused-argument
def get_hour_by_range(
    start: int = 0, end: int = 0, dt_format: str = FORMAT, **kwargs
) -> str:
    hour = randrange(start, end + 1)
    today = datetime.now()
    today = today.replace(hour=hour, minute=0, second=0, microsecond=0)
    return today.strftime(dt_format)


# pylint: enable=unused-argument


def get_end_depend_start(
    offset: int = 1, dt_format: str = FORMAT, **kwargs
) -> str:
    today_str: str = datetime.now().isoformat()
    today_str = kwargs.get('start_time', today_str)
    today: datetime = parser.parse(today_str)
    today = today + timedelta(hours=offset)
    return today.strftime(dt_format)
