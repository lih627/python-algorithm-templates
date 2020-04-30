class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        def bfs(i, j):
            mark = board[i][j]
            from collections import deque
            que = deque()
            que.append([i, j])
            visited[i][j] = True
            while que:
                x, y = que.popleft()
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    xx = x + dx
                    yy = y + dy
                    if -1 < xx < row and -1 < yy < col and board[xx][yy] == mark and not visited[xx][yy]:
                        que.append([xx, yy])
                        visited[xx][yy] = True
            # print(i, j, visited)
            return

        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]

        for i in range(col):
            if board[0][i] == 'O' and not visited[0][i]:
                bfs(0, i)
            if board[row - 1][i] == 'O' and not visited[row - 1][i]:
                bfs(row - 1, i)
        for i in range(row):
            if board[i][0] == 'O' and not visited[i][0]:
                bfs(i, 0)
            if board[i][col - 1] == 'O' and not visited[i][col - 1]:
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] != 'X' and not visited[i][j]:
                    board[i][j] = 'X'
