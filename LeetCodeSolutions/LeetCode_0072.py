class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = list(range(n + 1))
        for idx, _ in enumerate(dp):
            _[0] = idx

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

    def minDistance_2(self, word1: str, word2: str) -> int:
        '''
        自顶向下 递归方法
        leetcode: powcai
        '''
        from functools import lru_cache
        @lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            inserted = helper(i, j + 1)
            deleted = helper(i + 1, j)
            replaced = helper(i + 1, j + 1)
            return min(inserted, deleted, replaced) + 1

        return helper(0, 0)
