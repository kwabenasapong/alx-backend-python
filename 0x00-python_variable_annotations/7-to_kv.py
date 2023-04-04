#!/usr/bin/env python3

"""7. Complex types - string and int/float to tuple
"""

from typing import Union, Tuple


mxd = Union[int, float]


def to_kv(k: str, v: mxd) -> Tuple[str, float]:
    return (k, v**2)
