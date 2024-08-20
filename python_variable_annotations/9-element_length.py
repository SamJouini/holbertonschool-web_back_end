#!/usr/bin/env python3
"""Create a list of tuples where each tuple contains
a string from the input and its length."""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Create a list of tuples where each tuple contains
    a string from the input and its length.
    Returns a list of tuples, each containing a string and its length."""
    return [(i, len(i)) for i in lst]
