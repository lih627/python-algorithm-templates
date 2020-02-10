class Solution:
    def countDigitOne(self, n: int) -> int:
        tmp = 1
        res = 0
        while n >= tmp:
            a = n // tmp
            b = n % tmp
            res += (a + 8) // 10 * tmp + (a % 10 == 1) * (b + 1)
            tmp *= 10
        return res
