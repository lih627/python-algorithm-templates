class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n + 1):
            res = (res + m) % i
        return res
