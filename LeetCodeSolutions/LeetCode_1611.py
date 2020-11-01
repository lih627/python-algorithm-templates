class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Gray Code
        :param n:
        :return:
        """
        tmp = n
        cnt = 0
        while tmp:
            tmp >>= 1
            cnt += 1
        ret = 0
        for i in range(cnt - 1, -1, -1):
            c = (n >> i) & 1
            t = ret & 1 ^ c
            ret = (ret << 1) + t
        return ret
