#!/usr/bin/env python3
"""
	COmmenting
"""

from typing import Sequence, Optional, Any

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the sequence if it exists, otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
    Optional[Any]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]  # Return the first element if the list is not empty
    else:
        return None  # Return None if the list is empty
