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


#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
def dfs(i, j, board, visited, row, col):
    for [dx, dy] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        x = i + dx
        y = j + dy
        # print("xy {} {}".format(x, y))
        if -1 < x < row and -1 < y < col and board[x][y] == 'O' and (x, y) not in visited:
            # print("add {} {}".format(x, y))
            visited.add((x, y))
            # print("dfs {} {}".format(x, y))
            dfs(x, y, board, visited, row, col)
            # print('visited ', visited)
    return None


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        row, col = len(board), len(board[0])
        visited = set()

        for i in range(row):
            if board[i][0] == 'O':
                visited.add((i, 0))
                dfs(i, 0, board, visited, row, col)
            if board[i][col - 1] == 'O':
                visited.add((i, col - 1))
                dfs(i, col - 1, board, visited, row, col)
        for j in range(col):
            if board[0][j] == 'O':
                visited.add((0, j))
                dfs(0, j, board, visited, row, col)
            if board[row - 1][j] == 'O':
                visited.add((row - 1, j))
                dfs(row - 1, j, board, visited, row, col)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        return None

# @lc code=end
