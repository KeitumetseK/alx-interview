#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        last_row = triangle[-1]
        new_row = [1]  # Start with the first 1
        
        # Compute the values for the new row
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        
        new_row.append(1)  # End with the last 1
        triangle.append(new_row)

    return triangle  
