class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        for s in str:
            if 'A' <= s <= 'Z':
                res += chr(ord(s) + 32)
            else:
                res += s
        return res
