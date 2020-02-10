class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for ans in range(len(nums)):
            if nums[ans] == target:
                return ans
            if nums[ans] > target:
                return ans
        return len(nums)
