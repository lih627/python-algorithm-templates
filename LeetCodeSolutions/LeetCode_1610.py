import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        n = len(points)
        angles = [0] * n
        cnt = 0
        for idx, [x, y] in enumerate(points):
            if [x, y] == location:
                cnt += 1
                continue
            angles[idx] = math.atan2(y - location[1], x - location[0]) + math.pi
        angles.sort()
        angles = angles + [_ + math.pi * 2 for _ in angles]
        eps = angle / 180.0 * math.pi
        l, r = 0, 0
        ret = 0
        while r < len(angles):
            while angles[r] - angles[l] > eps:
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret + cnt
