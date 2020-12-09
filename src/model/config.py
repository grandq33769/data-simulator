# Standard Library
from dataclasses import dataclass
from typing import Callable, List, Union
from urllib.parse import ParseResult

from .model import Base, DataModel


@dataclass
class Authorization(Base):
    token: str = ''
    schema: str = 'Bearer'


@dataclass
class Environment(Base):
    auth: Union[Authorization, None] = None
    db_url: Union[ParseResult, None] = None
    endpoint: Union[ParseResult, None] = None


@dataclass
class Config(Base):
    module: str
    env: Environment
    data: List[DataModel]


@dataclass
class ExecuteType(Base):
    func: Callable
    date_format: str
