class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        mid = 0
        left = 0
        right = sum(nums[mid + 1:])
        if left == right:
            return mid
        while mid < len(nums) - 1 and left != right:
            left += nums[mid]
            right -= nums[mid + 1]
            # print(left, right, mid)
            mid += 1
        if left == right:
            return mid
        return -1
