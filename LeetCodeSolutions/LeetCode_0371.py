class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a = a ^ b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)
