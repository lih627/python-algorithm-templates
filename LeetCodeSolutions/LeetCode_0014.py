from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        n = min([len(_) for _ in strs])
        if n < 1:
            return ''
        res = ''
        i = 0
        while i < n:
            s = [_[i] for _ in strs]
            tmp = s[0]
            s = set(s)
            if len(s) == 1:
                res += tmp
            else:
                break
            i += 1
        return res
