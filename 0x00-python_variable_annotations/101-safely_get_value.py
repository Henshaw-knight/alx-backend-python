#!/usr/bin/env python3
"""safely_get_value module"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None]
        ) -> Union[Any, T]:
    """Returns the value of the key in dct if present else
    returns default value"""
    if key in dct:
        return dct[key]
    else:
        return default
