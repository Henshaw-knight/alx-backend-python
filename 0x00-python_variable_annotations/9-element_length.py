#!/usr/bin/env python3
"""element_length function module"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the list of tuples"""
    return [(i, len(i)) for i in lst]
