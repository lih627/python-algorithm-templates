class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def bfs(x, y):
            cnt = 0
            que = collections.deque()
            que.append([x, y])
            visited = set()
            visited.add((x, y))
            while que:
                x, y = que.popleft()
                grid[x][y] = 0
                cnt += 1
                for dx, dy in dirs:
                    xx = dx + x
                    yy = dy + y
                    if -1 < xx < m and -1 < yy < n and grid[xx][yy] and (xx, yy) not in visited:
                        que.append([xx, yy])
                        visited.add((xx, yy))
            return cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, bfs(i, j))
        return res
