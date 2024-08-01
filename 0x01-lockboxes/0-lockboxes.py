#!/usr/bin/python3
"""
This module provides a function to determine if all lockboxes can be unlocked.
"""

from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (List[List[int]]): A list of lists where each sublist represents keys contained in a box.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)

