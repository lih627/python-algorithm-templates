class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        lst = n % 3
        if lst == 1:
            return 3 ** (n // 3 - 1) * 4
        elif lst == 0:
            return 3 ** (n // 3)
        else:
            return 3 ** (n // 3) * lst
