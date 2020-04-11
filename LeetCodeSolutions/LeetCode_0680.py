class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                a = s[i + 1: j + 1]
                b = s[i: j]
                return a == a[::-1] or b == b[::-1]
        return True
