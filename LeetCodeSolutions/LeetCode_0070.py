class Solution:
    def climbStairs(self, n: int) -> int:
        pre, cur = 1, 0
        if not n: return n
        for _ in range(n + 1):
            tmp = pre + cur
            pre = cur
            cur = tmp
        return cur
