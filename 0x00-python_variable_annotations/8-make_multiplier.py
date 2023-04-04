#!/usr/bin/env python3

"""8. Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[summary]
    - make_multiplier
    - takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): [description] - multiplier

    Returns:
        Callable[[float], float]: [description] - function that multiplies
        a float by multiplier.
    """
    def multiply_by(x: float) -> float:
        """[summary] - function that multiplies a float by multiplier.

        Args:
            x (float): [description] - float to multiply

        Returns:
            float: [description] - result of multiplication
        """
        return (x * multiplier)
    return multiply_by
