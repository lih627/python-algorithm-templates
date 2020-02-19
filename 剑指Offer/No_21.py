class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            if nums[j] & 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j -= 1
        return nums
