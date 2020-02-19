class Solution:
    def hammingWeight(self, n: int) -> int:
        n &= 0xFFFFFFFF
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt
