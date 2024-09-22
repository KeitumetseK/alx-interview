# 0x08. Making Change

## Description
This project is about solving the "Making Change" problem, where given a pile of coins of different values, the goal is to determine the fewest number of coins needed to meet a given total amount.

The solution implements a dynamic programming approach to calculate the minimum number of coins required. If it's not possible to meet the total with the given coins, the program will return `-1`.

## Requirements
- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All code follows PEP 8 style (version 1.7.x).
- Each file ends with a new line and is executable.
- The repository includes a mandatory `README.md` file.

## Files
| Filename               | Description                                                  |
|------------------------|--------------------------------------------------------------|
| `0-making_change.py`    | Python function that solves the making change problem.       |
| `0-main.py`             | Main file to test the `makeChange` function.                 |

## Function Prototype
```python
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    Args:
        coins (list): List of available coin denominations.
        total (int): The total amount to reach.
    Returns:
        int: Fewest number of coins needed, or -1 if it's not possible.
    """

