class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[_] for _ in range(0, len(nums), 2)])
