#!/usr/bin/env python3

"""9. Let's duck type an iterable object
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the length of each element in the list.

    Args:
        lst (Iterable[Sequence]): The list to be evaluated.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing the
        elements and their lengths.
    """
    return [(i, len(i)) for i in lst]
