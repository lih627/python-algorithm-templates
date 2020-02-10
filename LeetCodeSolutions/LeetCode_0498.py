class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        lst_i, lst_j = 0, 0
        for _ in range(0, m + n - 1):
            if _ & 1:
                j = lst_j
                i = _ - j
                while -1 < i < m and -1 < j < n:
                    res.append(matrix[i][j])
                    i += 1
                    j -= 1
                if i == m:
                    lst_i = m - 1
                else:
                    lst_i = i

            else:
                i = lst_i
                j = _ - i
                while -1 < i < m and -1 < j < n:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1
                if j == n:
                    lst_j = n - 1
                else:
                    lst_j = j
        return res
