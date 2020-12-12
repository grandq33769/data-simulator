# Standard Library
from dataclasses import dataclass, fields
from typing import Any, Callable, Dict, List


@dataclass
class Base:
    @classmethod
    def fields(cls):
        return [a.name for a in fields(cls)]


@dataclass
class _DataModelBase(Base):
    scope: str
    frequency: List[str]
    callback: Callable


@dataclass
class _DataModelDefaultBase(Base):
    quantity: int = 1


@dataclass
class Attribute(Base):
    get: Callable
    args: Dict[str, Any]


@dataclass
class DataModel(_DataModelDefaultBase, _DataModelBase):
    def get_attributes(self):
        return [
            name
            for name in self.fields()
            if isinstance(getattr(self, name), Attribute)
        ]
