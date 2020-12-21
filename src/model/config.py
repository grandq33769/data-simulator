# Standard Library
from dataclasses import dataclass
from typing import List, Optional
from urllib.parse import ParseResult

from .base import Base
from .data import Callback, DataModel


@dataclass
class _AuthorizationBase(Base):
    path: str
    callback: Callback


@dataclass
class _AuthorizationDefaultBase:
    token: str = ''
    schema: str = 'Bearer'


@dataclass
class Authorization(_AuthorizationDefaultBase, _AuthorizationBase):
    def get(self) -> dict:
        return {'token': self.token}


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
