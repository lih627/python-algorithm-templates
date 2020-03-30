from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m = n = 8
        rx, ry = None, None

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rx, ry = i, j
                    break
            if rx is not None:
                break
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0
        for dx, dy in dirs:
            x = rx + dx
            y = ry + dy
            while -1 < x < 8 and -1 < y < 8:
                if board[x][y] == 'B':
                    break
                if board[x][y] == 'p':
                    res += 1
                    break
                x += dx
                y += dy
        return res
