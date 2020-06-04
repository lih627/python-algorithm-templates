class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        f = [-1] * (target + 1)
        f[0] = 0
        for i in range(8, -1, -1):
            for v in range(cost[i], target + 1):
                f[v] = max(f[v], f[v - cost[i]] * 10 + i + 1)
        return str(f[-1]) if f[-1] >= 0 else '0'
