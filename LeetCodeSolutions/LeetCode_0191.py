class Solution:
    def hammingWeight(self, n: int) -> int:
        n &= 0xFFFFFFFF
        n = bin(n)[2:]
        return n.count('1')
