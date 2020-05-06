class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        zeros = 0
        while m != n:
            m >>= 1
            n >>= 1
            zeros += 1
        return m << zeros
