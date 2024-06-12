#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (list of list of int): 2D matrix to rotate

    Returns:
    None: The matrix is rotated in-place
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
