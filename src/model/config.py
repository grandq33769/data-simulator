# Standard Library
from dataclasses import dataclass
from typing import List, Optional
from urllib.parse import ParseResult, urlparse

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
    db_url: Optional[str] = None
    endpoint: Optional[str] = None


@dataclass
class Environment(_EnvironmentDefaultBase, _EnvironmentBase):
    def __post_init__(self):
        if self.db_url is not None:
            self.db_url: ParseResult = urlparse(self.db_url)

        if self.endpoint is not None:
            self.endpoint: ParseResult = urlparse(self.endpoint)


@dataclass
class Config(Base):
    env: Environment
    data: List[DataModel]
