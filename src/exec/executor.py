# Standard Library
from datetime import datetime

# Third Party Library
import schedule
from loguru import logger as log

# Local Module
from src.model.config import ExecuteType

SCHEDULE = schedule

MAPPING = {
    'minute': ExecuteType(SCHEDULE.every().minute, ':%S'),
    'hour': ExecuteType(SCHEDULE.every().hour, ':%M'),
    'day': ExecuteType(SCHEDULE.every().day, '%H:%M'),
}


def every(scope: str, dt: datetime):
    try:
        exec_type = MAPPING[scope]
        date_str = dt.strftime(exec_type.date_format)
        return exec_type.func.at(date_str)
    except KeyError:
        log.exception(f'Can not get key "{scope}"')
    except Exception:
        log.exception('', diagnose=True)
