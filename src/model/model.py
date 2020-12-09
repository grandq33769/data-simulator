# Standard Library
from dataclasses import dataclass, fields
from typing import Any, Callable, Dict, List


@dataclass
class Base:
    @classmethod
    def fields(cls):
        return [a.name for a in fields(cls)]


@dataclass
class Attribute(Base):
    default: Any
    get: Callable
    args: Dict[str, Any]


@dataclass
class DataModel(Base):
    __attr__: List[str]
    name: str
    scope: str
    frequency: List[int]
    callback: Callable
    quantity: int = 1
