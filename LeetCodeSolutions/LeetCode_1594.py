class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0, 0] for _ in range(col)]
        havezero = False
        for nums in grid:
            for _ in nums:
                if _ == 0:
                    havezero = True
                    break
        for c in range(col):
            if c == 0:
                dp[0] = [max(grid[0][0], 0), min(grid[0][0], 0)]
                continue
            dp[c][0] = max(dp[c - 1][0] * grid[0][c], dp[c - 1][1] * grid[0][c])
            dp[c][1] = min(dp[c - 1][0] * grid[0][c], dp[c - 1][1] * grid[0][c])
        for r in range(1, row):
            cdp = [[0, 0] for _ in range(col)]
            for c in range(col):
                if c == 0:
                    cdp[c][0] = max(dp[c][0] * grid[r][c], dp[c][1] * grid[r][c])
                    cdp[c][1] = min(dp[c][0] * grid[r][c], dp[c][1] * grid[r][c])
                    continue
                cdp[c][0] = max(dp[c][0] * grid[r][c], dp[c][1] * grid[r][c],
                                cdp[c - 1][0] * grid[r][c], cdp[c - 1][1] * grid[r][c])
                cdp[c][1] = min(dp[c][0] * grid[r][c], dp[c][1] * grid[r][c],
                                cdp[c - 1][0] * grid[r][c], cdp[c - 1][1] * grid[r][c])
            dp = cdp
        if dp[-1][0] == 0:
            if havezero:
                return 0
            else:
                return -1
        return dp[-1][0] % (10 ** 9 + 7)
