#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        row, col = len(matrix), len(matrix[0])
        t1 = [[False for _ in range(col)] for _ in range(row)]
        t2 = [[False for _ in range(col)] for _ in range(row)]
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]

        def dfs(i, j, t):
            if t[i][j] == True:
                return
            t[i][j] = True
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if -1 < x < row and -1 < y < col and matrix[x][y] >= matrix[i][j]:
                    if not t[x][y]:
                        dfs(x, y, t)

        for i in range(row):
            dfs(i, 0, t1)
            dfs(i, col - 1, t2)
        for j in range(col):
            dfs(0, j, t1)
            dfs(row - 1, j, t2)
        ret = []
        for i in range(row):
            for j in range(col):
                if t1[i][j] and t2[i][j]:
                    ret.append([i, j])
        return ret

# @lc code=end
