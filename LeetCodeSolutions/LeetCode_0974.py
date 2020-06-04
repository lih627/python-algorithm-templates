class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {0: 1}
        m, ans = 0, 0
        for elem in A:
            m = (m + elem) % K
            t = d.get(m, 0);
            ans += t
            d[m] = t + 1
        return ans
