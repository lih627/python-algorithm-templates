from functools import lru_cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ret = 0
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                    ret += 1
                elif j == i + 1:
                    dp[i][j] = s[i] == s[j]
                    if dp[i][j]: ret += 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        ret += 1
        return ret
