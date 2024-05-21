#!/usr/bin/env python3
"""sum_mixed_list function module"""
from typing import List, Union


def sum_mixed_list(mxd: List[Union[int, float]]) -> float:
    """Returns the sum of the integers/floats in the list"""
    return float(sum(mxd))
