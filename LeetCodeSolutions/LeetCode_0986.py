#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(A), len(B)
        ret = []
        i, j = 0, 0
        while i < n1 and j < n2:
            interval1 = A[i]
            interval2 = B[j]
            if interval1[0] > interval2[1]:
                j += 1
            elif interval1[1] < interval2[0]:
                i += 1
            else:
                l = max(interval1[0], interval2[0])
                if interval1[1] <= interval2[1]:
                    r = interval1[1]
                    i += 1
                else:
                    r = interval2[1]
                    j += 1
                ret.append([l, r])
        return ret

# @lc code=end
