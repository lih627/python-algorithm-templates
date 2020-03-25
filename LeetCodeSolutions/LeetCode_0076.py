class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        d = {}
        for _ in t:
            if _ not in d:
                d[_] = 1
            else:
                d[_] += 1
        matched = set()
        import collections
        dd = collections.defaultdict(int)
        l = r = 0
        res = [-1, -1]
        min_len = float('inf')
        while r < len(s):
            if s[r] in d:
                dd[s[r]] += 1
                if dd[s[r]] >= d[s[r]]:
                    matched.add(s[r])
            while len(matched) == len(d.keys()):
                tmp = s[l]
                if tmp in d:
                    if dd[tmp] - 1 >= d[tmp]:
                        dd[tmp] -= 1
                    else:
                        if r - l + 1 < min_len:
                            min_len = r - l + 1
                            res = [l, r]
                        dd[tmp] -= 1
                        matched.remove(tmp)
                l += 1
            r += 1
        return s[res[0]: res[1] + 1]
