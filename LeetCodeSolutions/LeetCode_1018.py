class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        prefix = []
        for idx, val in enumerate(A):
            if idx == 0:
                prefix.append(val)
            else:
                prefix.append(val + (prefix[-1] << 1))
        res = []
        for v in prefix:
            res.append(v % 5 == 0)
        return res
