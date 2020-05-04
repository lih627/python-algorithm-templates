class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        def inline(x, y, lx1, ly1, lx2, ly2):
            if lx1 - lx1 == 0:
                t = (y - ly1) / (ly2 - ly1)
            elif y2 - y1 == 0:
                t = (x - lx1) / (ly2 - ly1)
            else:
                t = (y - ly1) / (ly2 - ly1)
            return 0 <= t <= 1

        def helper(x1, y1, x2, y2, x3, y3, x4, y4):
            res = []
            if inline(x1, y1, x3, y3, x4, y4):
                res.append([x1, y1])
            if inline(x2, y2, x3, y3, x4, y4):
                res.append([x2, y2])
            if inline(x3, y3, x1, y1, x2, y2):
                res.append([x3, y3])
            if inline(x4, y4, x1, y1, x2, y2):
                res.append([x4, y4])
            if res:
                return sorted(res)[0]
            else:
                return []

        if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                return helper(x1, y1, x2, y2, x3, y3, x4, y4)
            else:
                return []
        else:
            t1 = ((x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)) / \
                 ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 - x3) / (x4 - x3) + (x2 - x1) / (x4 - x3) * t1
            if 0 <= t1 <= 1 and 0 <= t2 <= 1:
                return [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]
            else:
                return []
