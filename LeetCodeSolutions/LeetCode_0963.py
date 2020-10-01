class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        d = collections.defaultdict(list)
        for px, py in itertools.combinations(points, 2):
            mx = (px[0] + py[0]) / 2
            my = (px[1] + py[1]) / 2
            r2 = (px[0] - py[0]) ** 2 + (px[1] - py[1]) ** 2
            d[mx, my, r2].append(px)
        ret = float('inf')
        for (cx, cy, r2), ps in d.items():
            for px, py in itertools.combinations(ps, 2):
                a = math.sqrt((px[0] - py[0]) ** 2 + (px[1] - py[1]) ** 2)
                pz = [px[0] + 2 * (cx - px[0]), px[1] + 2 * (cy - px[1])]
                b = math.sqrt((pz[0] - py[0]) ** 2 + (pz[1] - py[1]) ** 2)
                ret = min(ret, a * b)
        return ret if ret < float('inf') else 0
