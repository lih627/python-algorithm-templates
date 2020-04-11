class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        used = set()
        n = len(s)
        for i in range(n):
            ss, tt = s[i], t[i]
            if ss not in d:
                d[ss] = tt
                if tt in used:
                    return False
                used.add(tt)
            else:
                if d[ss] != tt:
                    return False

        return True
