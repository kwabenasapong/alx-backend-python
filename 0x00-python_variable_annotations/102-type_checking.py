#!/usr/bin/env python3

"""Type Checking"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom array"""
    zoomed_in: list = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array, 1)

zoom_3x = zoom_array(array, int(3.0))
