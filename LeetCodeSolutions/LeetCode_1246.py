from typing import List


class Solution:
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
                for k in range(i, j):
                    res = min(res, helper(i, k) + helper(k + 1, j))
                return res

        return helper(0, len(arr) - 1)

    def minimumMoves_2(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1 for j in range(n)] for i in range(n)]
        for gap in range(1, n):
            for i in range(n):
                if i + gap >= n:
                    break
                j = i + gap
                dp[i][j] = float('inf') if arr[i] != arr[j] else dp[i + 1][j - 1]
                for k in range(i, j):
                    if arr[i] == arr[k]:
                        # k可以解释为分割位置
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]
