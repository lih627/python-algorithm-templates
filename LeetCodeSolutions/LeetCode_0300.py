class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for idx, _ in enumerate(nums):
            for j in range(idx + 1, n):
                if nums[j] > _:
                    dp[j] = max(dp[j], dp[idx] + 1)
        return max(dp)
