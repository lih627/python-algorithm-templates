class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        '''
        ans = 0
        def backtrack(cur_m, cur_n):
            if cur_m == m and cur_n == n:
                nonlocal ans
                ans += 1
                return 
            if cur_m < m:
                backtrack(cur_m + 1, cur_n)
            if cur_n < n:
                backtrack(cur_m, cur_n + 1)
        backtrack(1, 1)
        return ans
        '''
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        print(dp)
        return dp[-1][-1]
