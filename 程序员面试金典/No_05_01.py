class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        m = 0
        for _ in range(i, j + 1):
            m <<= 1
            m += 1
        N &= 0xFFFFFFFF ^ (m << i)
        return N | (M << i)
