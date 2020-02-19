class Solution:
    def fib(self, n: int) -> int:
        pre = 1
        ppre = 0
        if n < 2:
            return n
        n -= 1
        while n:
            cur = pre + ppre
            pre, ppre = cur, pre
            n -= 1
        return cur % (10 ** 9 + 7)
