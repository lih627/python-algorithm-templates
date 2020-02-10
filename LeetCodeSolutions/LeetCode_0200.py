class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS or DFS
        """
        if not grid: return 0
        from collections import deque
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                cur_i, cur_j = i + x, j + y
                if -1 < cur_i < row and -1 < cur_j < col and grid[cur_i][cur_j] == '1':
                    dfs(cur_i, cur_j)

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                i, j = queue.pop()
                grid[i][j] = '0'
                for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    cur_i, cur_j = i + x, j + y
                    if -1 < cur_i < row and -1 < cur_j < col and grid[cur_i][cur_j] == '1':
                        queue.append((cur_i, cur_j))

        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt
