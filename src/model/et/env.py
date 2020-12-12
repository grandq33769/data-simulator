# Standard Library
from dataclasses import dataclass

from ..config import Authorization, Config, Environment, _AuthorizationBase


@dataclass
class _ETAuthorizationBase(_AuthorizationBase):
    account: str
    password: str


@dataclass
class ETAuthorization(Authorization, _ETAuthorizationBase):
    pass


@dataclass
class ETEnvironment(Environment):
    def __post__init__(self):
        conditions = [
            self.auth is not None,
            self.endpoint is not None,
        ]
        if not all(conditions):
            raise TypeError('auth and endpoint must be specified')


@dataclass
class ETConfig(Config):
    env: ETEnvironment
