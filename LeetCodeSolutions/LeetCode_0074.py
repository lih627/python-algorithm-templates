class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while -1 < i < m and -1 < j < n:
            tmp = matrix[i][j]
            if tmp == target:
                return True
            elif tmp < target:
                i += 1
            else:
                j -= 1
        return False
