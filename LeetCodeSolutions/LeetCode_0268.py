class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for _ in range(len(nums) + 1):
            res += _
        return res - sum(nums)
