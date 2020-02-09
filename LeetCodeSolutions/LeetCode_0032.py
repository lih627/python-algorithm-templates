class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        res = 0
        for _ in range(len(s)):
            if _ > 0:
                if s[_] == '(':
                    dp[_] = 0
                if s[_] == ')':
                    if s[_ - 1] == '(':
                        dp[_] = dp[_ - 2] + 2
                    if s[_ - 1] == ')' and s[_ - dp[_ - 1] - 1] == '(':
                        dp[_] = dp[_ - 1] + 2 + dp[_ - dp[_ - 1] - 2]
                    if dp[_] > res:
                        res = dp[_]
        return res
