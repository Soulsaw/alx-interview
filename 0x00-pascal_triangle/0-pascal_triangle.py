#!/usr/bin/python3
"""Function to retrurn the pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle implementation"""
    pascal = []
    if n <= 0:
        pascal = []
    elif n == 1:
        pascal.append([1])
    elif n >= 2:
        pascal = [[1], [1, 1]]
        for i in range(2, n, 1):
            new_row = [1]
            for j in range(len(pascal[i - 1]) - 1):
                new_row.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            new_row.append(1)
            pascal.append(new_row)
    return pascal
