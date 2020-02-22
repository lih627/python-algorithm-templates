class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) or nums[left] != target:
            return 0
        idx1 = left

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # note that change to <=
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left - idx1
