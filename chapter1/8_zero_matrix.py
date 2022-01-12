import pytest

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = set()
    col = set()
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                row.add(x)
                col.add(y)
    for x in range(m):
        for y in range(n):
            if (x in row) or (y in col):
                matrix[x][y] = 0
    return matrix

class Test():
    def test_zero_matrix(self):
        matrix = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0], 
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ]
        assert zero_matrix(matrix) == expected