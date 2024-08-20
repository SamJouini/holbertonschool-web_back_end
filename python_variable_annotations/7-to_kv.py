#!/usr/bin/env python3
"Create a tuple from a string and the square of a number."

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and the square of a number.
    Returns a tuple containing the input string and
    the square of the input number as a float."""
    return (k, float(v ** 2))
