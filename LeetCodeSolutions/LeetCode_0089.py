from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0] * 2 ** n
        exp = 0
        l = r = 1
        for i in range(1, 2 ** n):
            res[i] += res[r - i] + 2 ** exp
            if i == r:
                exp += 1
                l = r + 1
                r = l + 2 ** exp - 1
        return res
