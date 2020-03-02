from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        m, n = len(matrix), len(matrix[0])

        def setNone(i, j):
            for _ in range(n):
                matrix[i][_] = None if matrix[i][_] != 0 else 0
            for _ in range(m):
                matrix[_][j] = None if matrix[_][j] != 0 else 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    setNone(i, j)

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][j] = 0
