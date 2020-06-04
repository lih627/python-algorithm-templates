class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if idx == val:
                return idx
        return -1
