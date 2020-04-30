class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if i == j:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        if i + 1 == j:
                            dp[i][j] = True
                        else:
                            dp[i][j] = dp[i + 1][j - 1]
        res = []
        substrs = []

        def helper(idx):
            if idx == n:
                res.append(substrs[:])
                return
            for i in range(idx, n):
                if dp[idx][i]:
                    substrs.append(s[idx: i + 1])
                    helper(i + 1)
                    substrs.pop()

        helper(0)
        return res
