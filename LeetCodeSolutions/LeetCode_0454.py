class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter, defaultdict
        cnt_a = Counter(A)
        cnt_b = Counter(B)
        cnt_c = Counter(C)
        cnt_d = Counter(D)
        res = 0
        ab = defaultdict(int)
        cd = defaultdict(int)
        for k1, v1 in cnt_a.items():
            for k2, v2 in cnt_b.items():
                ab[k1 + k2] += v1 * v2
        for k1, v1 in cnt_c.items():
            for k2, v2 in cnt_d.items():
                cd[k1 + k2] += v1 * v2
        for k, v in ab.items():
            if -k in cd:
                res += v * cd[-k]
        return res
