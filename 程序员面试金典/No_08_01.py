class Solution:
    def waysToStep(self, n: int) -> int:
        MOD = 1000000007
        pre = [1, 2, 4]
        if n <= 3:
            return pre[n - 1]
        for i in range(4, n + 1):
            cur = sum(pre) % MOD
            pre = pre[1:] + [cur]
        return pre[-1]
