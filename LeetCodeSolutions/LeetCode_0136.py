class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)
