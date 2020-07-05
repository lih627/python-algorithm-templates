class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        MOD = 10 ** 9 + 7
        left = 0
        right = len(nums) - 1
        ret = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ret += 2 ** (right - left)
                ret %= MOD
                left += 1
            else:
                right -= 1
        return ret
