class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        ispos = n > 0
        n = abs(n)
        res, tmp = 1, x
        while n:
            if n & 1:
                res *= tmp
            tmp *= tmp
            n >>= 1
        if not ispos:
            res = 1 / res
        return res
