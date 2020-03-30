class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return - 1
        from collections import deque
        visited = set()
        que = deque()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    que.append((i, j, 0))
                    visited.add((i, j))

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        if not que or len(visited) == row * col:
            return -1
        res = 0
        while que and len(visited) != row * col:
            x, y, cnt = que.popleft()
            for dx, dy in dirs:
                xx = x + dx
                yy = y + dy
                if -1 < xx < row and -1 < yy < col and (xx, yy) not in visited and grid[xx][yy] == 0:
                    visited.add((xx, yy))
                    res = max(res, cnt + 1)
                    que.append((xx, yy, cnt + 1))
        return res
