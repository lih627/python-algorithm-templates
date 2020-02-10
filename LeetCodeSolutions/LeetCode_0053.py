class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for idx, _ in enumerate(nums):
            if not idx:
                continue
            dp[idx] = _ + dp[idx - 1] if dp[idx - 1] > 0 else _
        return max(dp)
