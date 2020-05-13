class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        visited = set()
        from collections import deque
        que = deque()
        que.append([0, 0])
        visited.add((0, 0))
        d = {1: ['l', 'r'], 2: ['u', 'd'], 3: ['l', 'd'],
             4: ['r', 'd'], 5: ['u', 'l'], 6: ['u', 'r']}

        def helper(x, y, dirs):
            for dir_ in dirs:
                if dir_ == 'l':
                    l = y - 1
                    if -1 < l < n and (x, l) not in visited:
                        tmp = grid[x][l]
                        if tmp in {1, 4, 6}:
                            que.append([x, l])
                            visited.add((x, l))
                elif dir_ == 'r':
                    r = y + 1
                    if -1 < r < n and (x, r) not in visited:
                        tmp = grid[x][r]
                        if tmp in {1, 3, 5}:
                            que.append([x, r])
                            visited.add((x, r))
                elif dir_ == 'u':
                    u = x - 1
                    if -1 < u < m and (u, y) not in visited:
                        tmp = grid[u][y]
                        if tmp in {2, 3, 4}:
                            que.append([u, y])
                            visited.add((u, y))
                elif dir_ == 'd':
                    d = x + 1
                    if -1 < d < m and (d, y) not in visited:
                        tmp = grid[d][y]
                        if tmp in {2, 5, 6}:
                            que.append([d, y])
                            visited.add((d, y))
            return None

        while que:
            x, y = que.popleft()
            cur = grid[x][y]
            helper(x, y, d[cur])
            if (m - 1, n - 1) in visited:
                return True
        return False
