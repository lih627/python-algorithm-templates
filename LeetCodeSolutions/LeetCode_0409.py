from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        # print(c)
        res = sum([i >> 1 << 1 for i in c.values()])
        odd = 1 if any([i & 1 for i in c.values()]) else 0
        # print(odd)
        return res + odd
