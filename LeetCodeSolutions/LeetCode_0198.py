class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        preMax = 0
        curMax = nums[0]
        idx = 1
        while idx < len(nums):
            preMax, curMax = curMax, max(preMax + nums[idx], curMax)
            idx += 1
        return max(preMax, curMax)
        # def dynamic(idx):
        #     if idx < 0:
        #         return 0
        #     if idx == 0:
        #         return nums[0]
        #     return max(nums[idx] + dynamic(idx -2), dynamic(idx - 1))
        # return dynamic(len(nums) - 1)
