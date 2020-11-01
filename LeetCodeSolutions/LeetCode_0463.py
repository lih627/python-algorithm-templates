class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        que = deque()
        visited = set()
        ret = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    que.append((r, c))
                    visited.add((r, c))
                    break

        while que:
            x, y = que.popleft()
            cnt = 0
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                cx = x + dx
                cy = y + dy
                if -1 < cx < row and -1 < cy < col:
                    if grid[cx][cy]:
                        cnt += 1
                        if (cx, cy) not in visited:
                            visited.add((cx, cy))
                            que.append((cx, cy))
            ret += 4 - cnt
        return ret
