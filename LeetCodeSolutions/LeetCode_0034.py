from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Bineary Search
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums):
            return [-1, -1]
        if nums[left] == target:
            idx1 = left
        else:
            return [-1, -1]
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return [idx1, left - 1]
