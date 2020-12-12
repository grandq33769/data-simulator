# Standard Library
from dataclasses import dataclass
from typing import Callable, List, Union
from urllib.parse import ParseResult

from .model import Base, DataModel


@dataclass
class _AuthorizationBase(Base):
    token: str


@dataclass
class _AuthorizationDefaultBase:
    schema: str = 'Bearer'


@dataclass
class Authorization(_AuthorizationDefaultBase, _AuthorizationBase):
    pass


@dataclass
class Environment(Base):
    auth: Union[Authorization, None]
    db_url: Union[ParseResult, None]
    endpoint: Union[ParseResult, None]


@dataclass
class Config(Base):
    module: str
    env: Environment
    data: List[DataModel]


@dataclass
class ExecuteType(Base):
    func: Callable
    date_format: str
