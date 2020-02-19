class Solution:
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        pre = 1
        ppre = 1
        n -= 1
        while n:
            cur = pre + ppre
            pre, ppre = cur, pre
            n -= 1
        return cur % (10 ** 9 + 7)
