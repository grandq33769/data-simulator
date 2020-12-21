# Standard Library
from random import uniform


def get_float(**kwargs) -> float:
    start: int = kwargs.get('start', 0)
    end: int = kwargs.get('end', 10)
    digit: int = kwargs.get('digit', 1)

    volume: float = uniform(start, end)
    return round(volume, digit)
