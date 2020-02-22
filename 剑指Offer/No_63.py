class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        maxs = [1 for _ in range(len(prices) - 1)]
        for i in range(len(prices) - 2, -1, -1):
            if curr_max < prices[i + 1]:
                curr_max = prices[i + 1]
            maxs[i] = curr_max
        # print(maxs)
        stack = [-float('inf')]
        for i in range(len(prices) - 1):
            if maxs[i] - prices[i] > stack[-1]:
                stack.append(maxs[i] - prices[i])
        return stack[-1] if stack[-1] > 0 else 0
