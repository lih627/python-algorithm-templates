class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        cnt_0 = 0
        for idx in range(len(nums) - 1):
            if nums[idx] == 0:
                cnt_0 += 1
                continue
            if nums[idx] == nums[idx + 1]:
                return False
            if nums[idx + 1] - nums[idx] > 1:
                cnt_0 -= nums[idx + 1] - nums[idx] - 1
        return cnt_0 > -1
