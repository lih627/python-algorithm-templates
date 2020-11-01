from collections import defaultdict


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)
        for n, s, e in trips:
            d[s] += n
            d[e] -= n
        kvs = list(d.items())
        kvs.sort()
        cur = 0
        for _, n in kvs:
            cur += n
            if cur > capacity:
                return False
        return True
