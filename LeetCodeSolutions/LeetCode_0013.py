class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        pre = d[s[0]]
        i = 1
        while i < len(s):
            cur = d[s[i]]
            if pre < cur:
                res -= pre
            else:
                res += pre
            pre = cur
            i += 1
        res += pre
        return res
