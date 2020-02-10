class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # if x == y:
        #     return 0
        # x &= 0xFFFFFFFF
        # y &= 0xFFFFFFFF
        # x, y = bin(x)[2:], bin(y)[2:]
        # x = x.rjust(32, '0')
        # y = y.rjust(32, '0')
        # res = 0
        # for i, j in zip(x, y):
        #     # print(i, j )
        #     if i != j:
        #         res += 1
        # return res
        return bin(x ^ y).count('1')
