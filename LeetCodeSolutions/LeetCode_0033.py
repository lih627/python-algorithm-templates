from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            right = len(nums) - 1
        else:
            max_value_idx = left - 1
            if nums[0] > target:
                left = max_value_idx + 1
                right = len(nums) - 1
            elif nums[0] < target:
                left = 0
                right = max_value_idx
            else:
                return 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
