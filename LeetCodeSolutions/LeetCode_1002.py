from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ret = Counter(A[0])
        for word in A[1:]:
            tmp = Counter(word)
            r = {}
            for k in ret:
                if k in tmp:
                    r[k] = min(ret[k], tmp[k])
            ret = r
        s = ""
        for k in ret:
            s += k * ret[k]
        return list(s)
