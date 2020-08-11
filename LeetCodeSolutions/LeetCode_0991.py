#
# @lc app=leetcode.cn id=991 lang=python3
#
# [991] 坏了的计算器
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ret = 0
        while Y > X:
            if Y & 1:
                Y += 1
            else:
                Y //= 2
            ret += 1
        return ret + X - Y
# @lc code=end
