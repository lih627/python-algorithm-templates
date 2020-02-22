class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        tmp = 1
        while n >= tmp:
            a = n // tmp
            b = n % tmp
            cnt += (a + 8) // 10 * tmp + (a % 10 == 1) * (b + 1)
            tmp *= 10
        return cnt
