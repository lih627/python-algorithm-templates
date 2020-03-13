class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        # [0 buy, 1 sell, 2 have, 3 not]
        dp = [-prices[0] - fee, 0, -prices[0] - fee, 0]
        for i in range(1, len(prices)):
            pre = dp[:]
            dp[0] = max(pre[1], pre[3]) - prices[i] - fee
            dp[1] = max(pre[0], pre[2]) + prices[i]
            dp[2] = max(pre[2], dp[0])
            dp[3] = max(dp[1], pre[3])
        return max(dp[1], dp[3])
