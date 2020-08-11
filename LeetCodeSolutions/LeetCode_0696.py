#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n, [0] * n]
        for idx, val in enumerate(s):
            i = int(val)
            if idx == 0:
                dp[i][idx] = 1
                continue
            dp[i][idx] = 1 + dp[i][idx - 1]
        cnt = 0
        for i in range(1, n):
            c = 0 if dp[0][i] else 1
            if i - dp[c][i] > -1 and dp[(c + 1) % 2][i - dp[c][i]] >= dp[c][i]:
                cnt += 1
        return cnt
# @lc code=end
