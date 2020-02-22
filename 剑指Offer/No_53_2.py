class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums + list(range(n + 1)))
