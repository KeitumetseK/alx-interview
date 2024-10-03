
# 0x0A Prime Game

## Description

Maria and Ben are playing a prime number game. They take turns choosing a prime number from a set of consecutive integers starting from 1 up to `n` and removing that number and its multiples from the set. The player who cannot make a move loses. 

This project implements a Python function that determines the winner of multiple rounds of the game, assuming both players play optimally. Maria always goes first.

## Function Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List containing the value of n for each round.

    Returns:
        str or None: Name of the player with the most wins ('Maria' or 'Ben'), or None if the winner cannot be determined.
    """
```

### Parameters
- **x**: The number of rounds to be played.
- **nums**: A list of integers, where each integer represents the maximum number (`n`) for each round.

### Return
- Returns the name of the player who won the most rounds (`"Maria"` or `"Ben"`).
- Returns `None` if the winner cannot be determined.

## Example

```python
x = 5
nums = [2, 5, 1, 4, 3]
print(isWinner(x, nums))
```

**Output**:
```
Ben
```

### How it works
- Each round starts with a set of numbers from 1 to `n`. Maria picks first and chooses a prime number. Both Maria and Ben take turns removing the chosen prime and its multiples from the set.
- If no prime numbers remain for a player to pick, that player loses the round.
- The player with the most wins across all rounds is the overall winner.

## Files

| File                | Description |
|---------------------|-------------|
| `0-prime_game.py`    | Implementation of the `isWinner` function. |
| `main_0.py`          | Sample test file to run the function. |
| `README.md`          | This file, describing the project. |

## Requirements

- Python 3.4.3+
- The function must not import any external packages.
- The function should handle up to 10,000 rounds and values of `n` efficiently.
