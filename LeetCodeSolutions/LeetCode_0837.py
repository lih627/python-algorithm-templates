class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1
        if N >= K - 1 + W:
            return 1
        dp = [0] * (K + W)
        for i in range(K, N + 1):
            dp[i] = 1.0
        # dp(i) = 1/W (dp[i + 1] + dp[i + W])
        for idx in range(K - 1, -1, -1):
            if idx == K - 1:
                suffix = sum(dp[K:])
                dp[idx] = suffix / W
            else:
                suffix -= dp[idx + W + 1]
                suffix += dp[idx + 1]
                dp[idx] = suffix / W
        return dp[0]
