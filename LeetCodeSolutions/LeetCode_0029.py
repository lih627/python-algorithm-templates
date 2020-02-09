class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend ^ divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                tmp <<= 1
                i <<= 1
        res *= sign
        return res if -1 << 31 <= res <= (1 << 31) - 1 else (1 << 31) - 1
