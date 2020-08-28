class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            if i + 1 == j:
                return i
            ret = float('inf')
            for k in range(i, j + 1):
                ret = min(ret, k + max(dp(i, k - 1), dp(k + 1, j)))
            return ret

        return dp(1, n)
