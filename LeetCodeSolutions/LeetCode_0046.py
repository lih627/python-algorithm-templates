from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        n = len(nums)
        res = []
        tmp = [None for i in nums]
        used = [0 for i in nums]

        def permute_all(cur_idx):
            if cur_idx == n:
                res.append(tmp[:])
                return
            for i in range(n):
                if not used[i]:
                    tmp[cur_idx] = nums[i]
                    used[i] = 1
                    permute_all(cur_idx + 1)
                    used[i] = 0

        permute_all(0)
        return res
