class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set([str(_) for _ in range(1, 10)]) for _ in range(9)]
        col = [set([str(_) for _ in range(1, 10)]) for _ in range(9)]
        block = [set([str(_) for _ in range(1, 10)]) for _ in range(9)]
        positions = []
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if tmp == '.':
                    positions.append((i, j))
                else:
                    row[i].remove(tmp)
                    col[j].remove(tmp)
                    block[i // 3 * 3 + j // 3].remove(tmp)

        def backtrack(idx=0):
            if idx == len(positions):
                return True
            i, j = positions[idx]
            k = i // 3 * 3 + j // 3
            for val in row[i] & col[j] & block[k]:
                row[i].remove(val)
                col[j].remove(val)
                block[k].remove(val)
                if backtrack(idx + 1):
                    board[i][j] = val
                    return True
                row[i].add(val)
                col[j].add(val)
                block[k].add(val)
            return False

        backtrack()
