class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        INF = 2 ** 31 - 1
        m, n = len(rooms), len(rooms[0])
        from collections import deque
        que = deque()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    que.append((i, j, 0))
        while que:
            x, y, cnt = que.popleft()
            for dx, dy in dirs:
                xx = x + dx
                yy = y + dy
                if -1 < xx < m and -1 < yy < n and (xx, yy) not in visited and rooms[xx][yy] == INF:
                    rooms[xx][yy] = cnt + 1
                    visited.add((xx, yy))
                    que.append((xx, yy, cnt + 1))
