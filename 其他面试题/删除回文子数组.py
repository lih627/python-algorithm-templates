"""
微软 2020 笔试 和 LeetCode1246 题目意思一样

给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文
子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。

注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。

请你计算并返回从数组中删除所有数字所需的最少操作次数。

输入：arr = [1,3,4,1,5]
输出：3
解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。

"""

from typing import List


class Solution:
    """
    区间DP模板题, 设定
    dp[i, j] 为该区间的最小操作次数
    """

    def minimumMoves(self, arr: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def helper(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if j - i == 1 and arr[i] == arr[j]:
                return 1
            if arr[i] == arr[j]:
                return helper(i + 1, j - 1)
            else:
                res = float('inf')
                # 将大区间分隔成 2 个小区间
                # 大区间的最少操作次数为子区间的操作次数之和的最小值
                for k in range(i, j):
                    res = min(res, helper(i, k) + helper(k + 1, j))
                return res

        return helper(0, len(arr) - 1)
