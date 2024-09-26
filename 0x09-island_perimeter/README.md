# Island Perimeter Project

This project contains a Python function that calculates the perimeter of an island represented by 1s in a 2D grid.

## Requirements

- Python 3.4.3 on Ubuntu 20.04 LTS
- PEP 8 style (version 1.7)
- No module imports are allowed.

## Usage

To use the function, import it and pass a grid as an argument.

Example:
```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12

