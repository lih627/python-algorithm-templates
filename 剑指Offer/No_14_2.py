class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        lst = n % 3
        if lst == 1:
            res = 3 ** (n // 3 - 1) * 4
        elif lst == 0:
            res = 3 ** (n // 3)
        else:
            res = 3 ** (n // 3) * lst
        return res % (10 ** 9 + 7)
