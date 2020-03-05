class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if sum(map(sum, grid)) == 0:
            return 0
        from collections import deque
        que = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j, 0))
                    visited.add((i, j))
        if not que:
            return -1
        while que:
            i, j, cur = que.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + di, j + dj
                if -1 < x < m and -1 < y < n and (x, y) not in visited:
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        que.append((x, y, cur + 1))
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if grid[i][j] == 1:
                        return -1
        return cur
