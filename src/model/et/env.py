# Standard Library
from dataclasses import dataclass
from urllib.parse import ParseResult

from ..config import (
    Authorization,
    Config,
    Environment,
    _AuthorizationBase,
    _AuthorizationDefaultBase,
)


@dataclass
class _ETAuthorizationBase(_AuthorizationBase):
    account: str
    password: str


@dataclass
class ETAuthorization(
    Authorization, _AuthorizationDefaultBase, _ETAuthorizationBase
):
    pass


@dataclass
class ETEnvironment(Environment):
    auth: ETAuthorization
    endpoint: ParseResult


@dataclass
class ETConfig(Config):
    module = 'et'
    env: ETEnvironment
