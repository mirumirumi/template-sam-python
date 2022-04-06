from decimal import Decimal
from typing import NoReturn
from __future__ import annotations


def decimal_to_float(obj: object) -> float | NoReturn:
    if isinstance(obj, Decimal): return float(obj)
    raise TypeError
