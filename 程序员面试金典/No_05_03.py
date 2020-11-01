class Solution:
    def reverseBits(self, num: int) -> int:
        num &= 0xFFFFFFFF
        a, na = 0, 0
        ret = 0
        while num:
            if num & 1:
                a += 1
                na += 1
            else:
                a = na + 1
                na = 0
            ret = max(a, na, ret)
            num >>= 1
        ret = max(ret, na + 1)
        return min(ret, 32)
