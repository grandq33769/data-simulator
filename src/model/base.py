# Standard Library
from dataclasses import dataclass, fields


@dataclass
class Base:
    @classmethod
    def fields(cls):
        return [a.name for a in fields(cls)]

    @property
    def classname(self):
        return self.__class__.__name__
