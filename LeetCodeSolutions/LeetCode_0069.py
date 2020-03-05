class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        cur = x
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(pre - cur) < 1e-6:
                return int(cur)
