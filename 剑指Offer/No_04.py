class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while row > i > -1 and col > j > -1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
        return False
