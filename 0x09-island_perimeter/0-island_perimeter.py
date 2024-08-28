#!/usr/bin/python3
"""Doc of the island perimeter module"""


def island_perimeter(grid) -> int:
    """This function is aim to determinate the island perimeter"""
    perimeter = 0
    for i in range(len(grid)):
        if i == 0 or i == len(grid) - 1:
            continue
        for j in range(len(grid[i])):
            if j == 0 or j == len(grid[i]) - 1:
                continue
            if (grid[i][j] == 1):
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
