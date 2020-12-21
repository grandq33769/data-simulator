# Standard Library
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List

# Third Party Library
from dateutil import parser
from loguru import logger as log

from .base import Base
from .scheduler import MAPPING, SCHEDULE


def parse_dt(datetime_str: str, str_format: str) -> str:
    return parser.parse(datetime_str).strftime(str_format)


@dataclass
class Callback(Base):
    func: Callable
    kwargs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class _DataModelBase(Base):
    scope: str
    frequency: List[str]
    callback: Callback


@dataclass
class _DataModelDefaultBase(Base):
    jobs: List[SCHEDULE.Job] = field(default_factory=list)
    quantity: int = 1


@dataclass
class Attribute(Base):
    get: Callable
    kwargs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DataModel(_DataModelDefaultBase, _DataModelBase):
    def __post_init__(self):
        try:
            exec_type = MAPPING[self.scope]
            self.frequency = [
                parse_dt(datetime_str, exec_type.date_format)
                for datetime_str in self.frequency
            ]
            self.jobs = [
                lambda f=freq: exec_type.func().at(f)
                for freq in self.frequency
            ]
        except KeyError:
            log.exception(f'Can not get key "{self.scope}"')
        except Exception:
            log.exception('', diagnose=True)

    def get_attributes(self):
        return [
            name
            for name in self.fields()
            if isinstance(getattr(self, name), Attribute)
        ]
