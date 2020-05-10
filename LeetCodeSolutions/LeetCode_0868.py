class Solution:
    def binaryGap(self, N: int) -> int:
        str_n = bin(N)[2:]
        ans = 0
        idxs = []
        for idx, val in enumerate(str_n):
            if val == '1':
                if idxs:
                    ans = max(ans, idx - idxs[-1])
                idxs.append(idx)
        return ans
