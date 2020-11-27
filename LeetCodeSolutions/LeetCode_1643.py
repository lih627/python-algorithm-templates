import math
from functools import lru_cache


@lru_cache(None)
def comb(a, b):
    return math.comb(a, b)


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        nv, nh = destination
        ret = ''

        for _ in range(sum(destination)):
            if nv == 0:
                ret += 'H'
                nh -= 1
                continue
            if nh == 0:
                ret += 'V'
                nv -= 1
                continue
            # selecv_v = comb(nv + nh - 1, nh)
            select_h = comb(nv + nh - 1, nv)
            if select_h >= k:
                ret += 'H'
                nh -= 1
            else:
                k -= select_h
                ret += 'V'
                nv -= 1

        return ret
