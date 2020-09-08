#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
import functools


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        prefix = [0] * n
        for idx, val in enumerate(nums):
            if idx == 0:
                prefix[idx] = val
                continue
            prefix[idx] = val + prefix[idx - 1]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            if i + j == 1:
                return max(nums[i], nums[j])
            if i == 0:
                tmp = 0
            else:
                tmp = prefix[i - 1]
            ret = max(nums[i] + prefix[j] - prefix[i] - dp(i + 1, j),
                      nums[j] + prefix[j - 1] - tmp - dp(i, j - 1))
            return ret

        ret = dp(0, n - 1)
        return ret + ret >= prefix[-1]

# @lc code=end
