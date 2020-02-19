class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False
        n = len(word)
        row, col = len(board), len(board[0])
        visited = set()
        res = False

        def dfs(i, j, idx):
            nonlocal res
            if i in [-1, row] or j in [-1, col] or board[i][j] != word[idx]:
                return
            if (i, j) in visited:
                return
            if board[i][j] == word[idx]:
                if idx == n - 1:
                    res = True
                    return
                visited.add((i, j))
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if not res:
                        dfs(i + di, j + dj, idx + 1)
                visited.remove((i, j))

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
                if res: return True
        return False
