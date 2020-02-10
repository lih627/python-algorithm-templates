class Solution:
    def reverseWords(self, s: str) -> str:
        res, blank = '', False
        for _ in s[::-1]:
            res += _
        return ' '.join(res.split()[::-1])
