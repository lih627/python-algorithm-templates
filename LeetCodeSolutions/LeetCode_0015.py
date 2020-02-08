class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        res = []
        for left in range(n - 2):
            middle, right = left + 1, n - 1
            if nums[left] > 0 or nums[right] < 0:
                break
            if left > 0 and nums[left - 1] == nums[left]:
                continue
            while middle < right:
                curr_sum = nums[left] + nums[middle] + nums[right]
                if curr_sum > 0:
                    while right - 1 > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif curr_sum < 0:
                    while middle + 1 < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    middle += 1
                else:
                    res.append([nums[left], nums[middle], nums[right]])
                    while middle + 1 < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    middle += 1
                    while right - 1 > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
        return res
