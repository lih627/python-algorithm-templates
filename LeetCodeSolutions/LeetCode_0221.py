class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        ans = 0
        pre = []
        for val in matrix[0]:
            pre.append(int(val))
            if int(val) > ans:
                ans = int(val)

        for i in range(1, n):
            cur = [0] * m
            for j in range(m):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    cur[j] = 1
                else:
                    cur[j] = min(cur[j - 1], pre[j - 1], pre[j]) + 1
                if cur[j] > ans:
                    ans = cur[j]
            pre = cur
        return ans * ans
