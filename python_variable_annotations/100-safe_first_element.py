#!/usr/bin/env python3
"""
This script defines a function that safely returns the first element of a sequence.
If the sequence is empty, the function returns None.
"""

from typing import Sequence, Optional, Any

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of the sequence if it exists, otherwise return None.

    Parameters:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Optional[Any]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]  # Return the first element if the sequence is not empty
    return None  # Return None if the sequence is empty
