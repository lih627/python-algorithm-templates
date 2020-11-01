class Solution:
    def printBin(self, num: float) -> str:
        ret = "0."
        for i in range(32):
            c = num * 2
            if c >= 1.0:
                c -= 1
                ret += '1'
            else:
                ret += '0'
            if abs(c) < 1e-8:
                return ret
            num = c
        return 'ERROR'
