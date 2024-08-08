#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the minimum number of operations required
    to achieve exactly n 'H' characters in a file.

    Operations available:
    1. Copy All
    2. Paste

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed. If n is less than 1, returns 0.
    """
    if n <= 1:
        return 0
    
    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        remaining = n - current
        
        if remaining % current == 0:
            clipboard = current  # Copy All
            operations += 1
        
        current += clipboard  # Paste
        operations += 1
    
    return operations

