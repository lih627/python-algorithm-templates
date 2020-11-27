class Solution:
    def maxA(self, N: int) -> int:
        dp = [0, 1]
        for i in range(2, N + 1):
            dp.append(dp[-1] + 1)
            for k in range(i - 2, 0, -1):
                dp[-1] = max(dp[-1], dp[k] * (i - k - 1))
        return dp[-1]
