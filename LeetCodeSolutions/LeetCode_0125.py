class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        tmp = ''
        for _ in s:
            if '0' <= _ <= '9' or 'A' <= _ <= 'Z':
                tmp += _
        # n = len(tmp)
        i, j = 0, len(tmp) - 1
        while i < j:
            if tmp[i] != tmp[j]:
                return False
            i += 1
            j -= 1
        return True
