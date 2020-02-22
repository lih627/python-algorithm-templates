class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for idx, _ in enumerate(grid[0]):
            if idx == 0:
                dp[idx] = _
            else:
                dp[idx] = _ + dp[idx - 1]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = max(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]
