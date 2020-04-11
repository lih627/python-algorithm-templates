class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        from collections import Counter
        cnt = Counter(s)
        res = ''
        k_v = sorted([(k, v) for k, v in cnt.items()], key=lambda x: -x[1])
        for (k, v) in k_v:
            res += k * v
        return res
