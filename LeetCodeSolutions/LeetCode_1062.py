class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        lo, hi = 1, len(S)

        def isRepeat(l):
            n = len(S)
            visietd = set()
            for i in range(0, n - l + 1):
                tmp = S[i: i + l]
                if tmp in visietd:
                    return True
                visietd.add(tmp)
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            if isRepeat(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
