#!/usr/bin/python3
"""Doc of the rotate 2d matrix module"""


def rotate_2d_matrix(matrix) -> None:
    """Rotate a 2d matrix to a 90 degree
    Args:
        matrix (list of list): The 2d matrix

    Returns:
            matrix (list of list): In-place rotate a 2d matrix
    """
    n = len(matrix)
    for i in range(0, n//2, 1):
        for j in range(i, n - i - 1, 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp
