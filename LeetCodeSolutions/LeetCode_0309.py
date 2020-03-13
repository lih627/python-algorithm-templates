class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # dp [buy sell cooldown havestock nothavstock]
        dp = [-prices[0], 0, float('-inf'), -prices[0], 0]
        for i in range(1, len(prices)):
            pre = dp[:]
            price = prices[i]
            dp[0] = pre[4] - price
            dp[1] = max(pre[0], pre[3]) + price
            dp[2] = pre[1]
            dp[3] = max(dp[0], pre[3])
            dp[4] = max(pre[1], pre[2], pre[4])
        return max(dp[1], dp[2], dp[4])
