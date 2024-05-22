#!/usr/bin/env python3
"""make_multiplier function module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier"""
    def multiplier_func(value: float) -> float:
        """Function that multiplies the multiplier by a float (value)"""
        return value * multiplier
    return multiplier_func
