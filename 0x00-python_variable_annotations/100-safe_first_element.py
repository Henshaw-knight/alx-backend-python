#!/usr/bin/env python3
"""safe_first_element function module"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns either an element of a list or None"""
    if lst:
        return lst[0]
    else:
        return None
