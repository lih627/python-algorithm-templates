class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for _ in s:
            if _ == ' ':
                res += '%20'
            else:
                res += _
        return res
