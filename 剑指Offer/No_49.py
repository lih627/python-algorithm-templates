class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if not n:
            return 0
        res = [0] * n
        res[0] = 1
        p2 = p3 = p5 = 0
        for idx in range(1, n):
            r2 = res[p2] * 2
            r3 = res[p3] * 3
            r5 = res[p5] * 5
            res[idx] = min(r2, r3, r5)
            if res[idx] == r2: p2 += 1
            if res[idx] == r3: p3 += 1
            if res[idx] == r5: p5 += 1
        return res[-1]
