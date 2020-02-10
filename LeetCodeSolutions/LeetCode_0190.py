class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            tmp = n & 0x80000000
            tmp = 1 if tmp else 0
            n <<= 1
            if tmp:
                res += 2 ** _
            print(bin(res))
        return res
