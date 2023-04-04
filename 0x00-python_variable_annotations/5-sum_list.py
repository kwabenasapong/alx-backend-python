#!/usr/bin/env python3

"""5. Complex types - list of floats
"""


def sum_list(input_list: list[float]) -> float:
    sum: float = 0
    for x in input_list:
        sum += x
    return sum
