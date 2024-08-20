#!/usr/bin/env python3
"Create a function that multiplies a float by a given multiplier."

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.
    Returns a function that takes a float and returns a float."""
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
