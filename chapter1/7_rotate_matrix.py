import pytest

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i-1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            matrix[i][-layer - 1] = temp
    return matrix

class Test():
    def test_rotate_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert rotate_matrix(matrix) == [[9, 8, 7], [6, 5, 4], [3, 2, 1]]