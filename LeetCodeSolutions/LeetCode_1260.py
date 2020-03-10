class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        if k == m * n:
            return grid
        k %= m * n
        tmp = []
        for _ in grid:
            tmp += _
        tmp = tmp[-k:] + tmp[:-k]
        res = [[0] * n for _ in range(m)]
        for idx, val in enumerate(tmp):
            res[idx // n][idx - idx // n * n] = val
        return res
