class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.index(needle) if needle in haystack else -1
        # KMP
        if not needle:
            return 0

        def get_next(pat):
            _next = [0] * len(pat)
            _next[0] = -1
            i, j = 0, -1
            while i < len(pat) - 1:
                if j == -1 or pat[i] == pat[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]
            return _next

        _next = get_next(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = _next[j]

        if j == len(needle):
            return i - len(needle)
        else:
            return -1
