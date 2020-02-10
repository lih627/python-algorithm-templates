class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for _ in s:
            if _ not in d:
                d[_] = 1
            else:
                d[_] += 1
        for idx, _ in enumerate(s):
            if d[_] == 1: return idx
        return -1
