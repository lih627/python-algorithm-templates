class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for _ in range(1, len(prices)):
            tmp = prices[_] - prices[_ - 1]
            if tmp > 0:
                profit += tmp
        return profit
