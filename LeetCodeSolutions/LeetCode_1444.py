class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        nums = [[0 for _ in range(n)] for j in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                hasApple = 0
                if pizza[i][j] == 'A':
                    hasApple = 1
                if i == m - 1 and j == n - 1:
                    nums[i][j] = hasApple
                elif j == n - 1:
                    nums[i][j] = hasApple + nums[i + 1][j]
                elif i == m - 1:
                    nums[i][j] = hasApple + nums[i][j + 1]
                else:
                    nums[i][j] = hasApple + nums[i + 1][j] + nums[i][j + 1] - nums[i + 1][j + 1]
        MOD = 10 ** 9 + 7
        print(nums)
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j, cur_k):
            if cur_k == k and nums[i][j]:
                return 1
            if nums[i][j] == 0:
                return 0
            ans = 0
            cur_num = nums[i][j]
            for ii in range(i + 1, m):
                if nums[ii][j] < cur_num:
                    ans += dp(ii, j, cur_k + 1)
                ans %= MOD
            for jj in range(j + 1, n):
                if nums[i][jj] < cur_num:
                    ans += dp(i, jj, cur_k + 1)
                ans %= MOD
            return ans % MOD

        return dp(0, 0, 1)
