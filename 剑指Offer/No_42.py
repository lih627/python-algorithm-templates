class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = nums[0]
        cur_sum = 0
        for _ in nums:
            cur_sum += _
            pre_sum = max(pre_sum, cur_sum)
            if cur_sum <= 0:
                cur_sum = 0
        return pre_sum
