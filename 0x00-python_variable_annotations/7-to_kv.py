#!/usr/bin/env python3
"""to_kv function module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string `k` and an int OR float `v` as arguments and
    returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v which is
    annotated as a float"""
    tupl = (k, float(v ** 2))
    return tupl
