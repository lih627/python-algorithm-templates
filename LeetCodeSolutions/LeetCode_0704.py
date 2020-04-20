class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        if l == r:
            return -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return -1
