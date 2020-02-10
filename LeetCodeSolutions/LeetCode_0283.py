class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums0 = [i for i in nums if not i]
        nums1 = [i for i in nums if i]
        nums[:] = nums1 + nums0
