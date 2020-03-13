class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # [0 firstbuy, 1fsell, 2secondbuy, 3ssell]
        dp = [-prices[0], 0, float('-inf'), 0]
        for i in range(1, len(prices)):
            pre = dp[:]
            dp[0] = max(-prices[i], pre[0])
            dp[1] = max(prices[i] + pre[0], pre[1])
            dp[2] = max(pre[2], pre[1] - prices[i])
            dp[3] = max(pre[2] + prices[i], pre[3])
        return max(dp[1], dp[3])
