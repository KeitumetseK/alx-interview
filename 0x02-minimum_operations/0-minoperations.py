#!/usr/bin/python3
def minOperations(n):
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

