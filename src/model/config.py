# Standard Library
from dataclasses import dataclass
from typing import Callable, List, Optional
from urllib.parse import ParseResult

from .model import Base, DataModel


@dataclass
class _AuthorizationBase(Base):
    pass


@dataclass
class _AuthorizationDefaultBase:
    token: str = ''
    schema: str = 'Bearer'


@dataclass
class Authorization(_AuthorizationDefaultBase, _AuthorizationBase):
    pass


@dataclass
class _EnvironmentBase(Base):
    pass


@dataclass
class _EnvironmentDefaultBase:
    auth: Optional[Authorization] = None
    db_url: Optional[ParseResult] = None
    endpoint: Optional[ParseResult] = None


@dataclass
class Environment(_EnvironmentDefaultBase, _EnvironmentBase):
    pass


@dataclass
class Config(Base):
    env: Environment
    data: List[DataModel]


@dataclass
class ExecuteType(Base):
    func: Callable
    date_format: str
