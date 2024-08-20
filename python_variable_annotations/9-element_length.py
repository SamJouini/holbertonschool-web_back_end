#!/usr/bin/env python3
"""Create a list of tuples where each tuple contains
a string from the input and its length."""

from typing import Iterable, List, Tuple


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """    Create a list of tuples where each tuple contains a string from the input
    and its length.
    Returns a list of tuples, each containing a string and its length."""
    return [(i, len(i)) for i in lst]
