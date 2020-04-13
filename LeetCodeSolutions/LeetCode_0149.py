from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        from fractions import Fraction
        from collections import defaultdict
        cnt = defaultdict(int)
        n = len(points)
        max_points = 0
        for i in range(n):
            cnt.clear()
            duplicate = 1
            x1, y1 = points[i]
            cur_max = 0
            # 不需要从 0 开始统计, 并跳过 i
            # 从 i + 1 就可以
            # 比如 i = 3, 如果 j = 0 和 i = 3 构成的直线上面点最多
            # 在 i = 0, j = 3 的时候已经统计过了
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # 如果是相同的点, 记录相同点的个数
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue
                if x2 - x1 == 0:
                    # 如果斜率为inf 单独记录
                    cnt['inf'] += 1
                    if cnt['inf'] > cur_max:
                        cur_max = cnt['inf']
                else:
                    # 使用 Fraction 简化斜率计算
                    slope = Fraction(y2 - y1, x2 - x1)
                    cnt[slope] += 1
                    if cnt[slope] > cur_max:
                        cur_max = cnt[slope]
            # 当前的最大值为 同斜率贡献的点数 + 与当前点重复的点数
            cur_max += duplicate
            max_points = max(max_points, cur_max)
        return max_points
