from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        d = 0
        for s in seq:
            if s == '(':
                d += 1
                res.append(d % 2)
            else:
                res.append(d % 2)
                d -= 1
        return res
