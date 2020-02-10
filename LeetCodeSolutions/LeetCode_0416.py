class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        # nums.sort()
        if sums & 1:
            return False
        val = sums // 2
        dp = [0] * (val + 1)
        '''
        for _ in nums:
            for j in range(val, _ - 1, -1):
                dp[j] = max(dp[j - _] + _, dp[j]) if j - _ > -1 else dp[j]
                if dp[j] == val:
                    return True
        return False
        '''

        sums = sum(nums)
        if sums % 2 == 1:
            return False
        target = sums // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
            if dp[-1]:
                return True
        return dp[-1]
