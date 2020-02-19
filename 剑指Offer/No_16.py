class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        ispos = n > 0
        n = abs(n)
        tmp = x
        res = 1
        while n > 0:
            if n & 1:
                res *= tmp
            n >>= 1
            tmp *= tmp
        if not ispos:
            res = 1 / res
        return res
