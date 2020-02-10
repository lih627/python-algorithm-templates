class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxlen = nums[0]
        l = len(nums)
        for idx in range(l):
            if idx <= maxlen:
                cur_len = idx + nums[idx]
                if cur_len > maxlen:
                    maxlen = cur_len
            else:
                return False
        return True
