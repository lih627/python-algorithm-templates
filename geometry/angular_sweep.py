import math
from typing import List

"""
You have a very large square wall and a circular dartboard placed on 
the wall. You have been challenged to throw darts into 
the board blindfolded. Darts thrown at the wall are represented
 as an array of points on a 2D plane. 

Return the maximum number of points that are within or
 lie on any circular dartboard of radius r.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard
"""


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def helper(i, r, n):
            angles = []
            for j in range(n):
                if i != j and (l2 := sum([_ ** 2 for _ in vec[i][j]])) <= (2 * r) ** 2 + 1e-8:
                    C = math.acos(math.sqrt(l2) / (2 * r))
                    T = math.atan2(vec[i][j][1], vec[i][j][0])
                    _in = T - C
                    _out = T + C
                    angles.append([_in, True])
                    angles.append([_out, False])
            # 这里排序是重点, 考虑边界条件
            # 比如有 [0, False], [0, True]
            # 要让[0, True] 排到 [0, False]前面
            angles.sort(key=lambda x: [x[0], - x[1]])
            cnt = res = 1
            for item in angles:
                if item[1]:
                    cnt += 1
                else:
                    cnt -= 1
                if cnt > res:
                    res = cnt
            return res

        n = len(points)
        if n == 1:
            return 1
        # vec[i][j] = [Jx - Ix, J_y - Iy]
        # vec 存入两点之间的方向向量
        vec = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                JxIx = points[j][0] - points[i][0]
                JyIy = points[j][1] - points[i][1]
                vec[i][j] = [JxIx, JyIy]
                vec[j][i] = [-JxIx, -JyIy]
        ans = 0
        for i in range(n):
            ans = max(ans, helper(i, r, n))

        return ans
