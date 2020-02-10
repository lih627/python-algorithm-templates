class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 0
        res = 0
        while r < len(nums):
            if nums[l] == 1:
                if nums[r] == 1:
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    l = r + 1
                    r = l
            else:
                l += 1
                r = l
        return res
