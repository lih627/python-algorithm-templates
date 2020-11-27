class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        position = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                position[board[i][j]] = (i, j)
        pre = 'a'
        ret = ''
        for c in target:
            if c == pre:
                ret += '!'
                continue
            ppos = position[pre]
            cpos = position[c]
            dy, dx = [a - b for (a, b) in zip(cpos, ppos)]
            if pre == 'z':
                ret += abs(dy) * 'U'
                ret += 'R' * dx
            elif c == 'z':
                ret += abs(dx) * 'L'
                ret += dy * 'D'
            else:
                ret += dx * 'R' if dx > 0 else abs(dx) * 'L'
                ret += dy * 'D' if dy > 0 else abs(dy) * 'U'
            ret += '!'
            pre = c
        return ret
