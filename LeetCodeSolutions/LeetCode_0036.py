from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            d = set()
            for _ in row:
                if _ != '.':
                    if _ not in d:
                        d.add(_)
                    else:
                        return False

        for j in range(9):
            d = set()
            for i in range(9):
                _ = board[i][j]
                if _ != '.':
                    if _ not in d:
                        d.add(_)
                    else:
                        return False

        def judgeblock(i, j):
            d = set()
            for x in range(3):
                for y in range(3):
                    ii, jj = i + x, j + y
                    _ = board[ii][jj]
                    if _ != '.':
                        if _ not in d:
                            d.add(_)
                        else:
                            return False
            return True

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not judgeblock(i, j):
                    return False
        return True
