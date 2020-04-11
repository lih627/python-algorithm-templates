class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(n, k):
            if k == 0 or n == 0:
                return 0
            if k == 1:
                return n
            if n == 1:
                return 1
            lo, hi = 1, n
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                t1 = dp(mid, k - 1)
                t2 = dp(n - mid, k)
                if t1 < t2:
                    lo = mid
                elif t1 > t2:
                    hi = mid
                else:
                    lo = hi = mid
            return 1 + min([max(dp(m - 1, k - 1), dp(n - m, k)) for m in (lo, hi)])

        return dp(N, K)

    def superEggDrop2(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                dp[k] = dp[k] + dp[k - 1] + 1
        return m
