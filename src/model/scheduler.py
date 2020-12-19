# Standard Library
from dataclasses import dataclass
from typing import Callable

# Third Party Library
import schedule

SCHEDULE = schedule


@dataclass
class ExecuteType:
    func: Callable
    date_format: str


MAPPING = {
    'minute': ExecuteType(lambda: SCHEDULE.every().minute, ':%S'),
    'hour': ExecuteType(lambda: SCHEDULE.every().hour, ':%M'),
    'day': ExecuteType(lambda: SCHEDULE.every().day, '%H:%M'),
}
