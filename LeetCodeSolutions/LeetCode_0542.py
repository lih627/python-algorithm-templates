class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[None for k in _] for _ in matrix]
        row = len(matrix)
        col = len(matrix[0])
        from collections import deque
        def bfs(i, j):
            if matrix[i][j] == 0:
                return 0
            visited = set((i, j))
            que = deque()
            que.append((i, j, 0))
            f = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            while que:
                r, c, dist = que.popleft()
                dist += 1
                for x, y in f:
                    if -1 < r + x < row and -1 < c + y < col:
                        visited.add((r + x, c + y))
                        if matrix[r + x][c + y] == 0:
                            return dist
                        else:
                            que.append((r + x, c + y, dist))

        for i in range(row):
            for j in range(col):
                res[i][j] = bfs(i, j)
        return res
