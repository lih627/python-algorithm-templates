from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dx, dy in dirs:
                    x = dx + i
                    y = dy + j
                    if -1 < x < m and -1 < y < n and board[x][y] & 1:
                        cnt += 1
                board[i][j] += cnt << 1

        for i in range(m):
            for j in range(n):
                if board[i][j] & 1:
                    if board[i][j] >> 1 in [2, 3]:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if board[i][j] >> 1 == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
