# Standard Library
from dataclasses import dataclass
from typing import List
from urllib.parse import ParseResult

from .model import DataModel


@dataclass
class Authorization:
    token: str
    schema: str = 'Bearer'


@dataclass
class Environment:
    auth: Authorization
    db_url: ParseResult
    endpoint: ParseResult


@dataclass
class Config:
    module: str
    env: Environment
    data: List[DataModel]
