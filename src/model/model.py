# Standard Library
from dataclasses import dataclass
from typing import Any, Callable, Dict, List


@dataclass
class Attribute:
    default: Any
    get: Callable
    args: Dict[str, Any]


@dataclass
class DataModel:
    __attr__: List[str]
    name: str
    scope: str
    frequency: List[int]
    callback: Callable
    quantity: int = 1
