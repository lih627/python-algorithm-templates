class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(points)
        dist = defaultdict(int)
        res = 0
        for i in range(n):
            dist.clear()
            for j in range(n):
                if j == i:
                    continue
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                dist[dis] += 1
            for v in dist.values():
                res += v * v - v
        return res
