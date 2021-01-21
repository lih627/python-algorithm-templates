class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l, r, n = 0, 0, len(s)
        ret = []
        while r < n:
            while r < n and s[l] == s[r]:
                r += 1;
            if r - l > 2:
                ret.append([l, r - 1])
            l = r
        return ret
