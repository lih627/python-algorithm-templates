class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r, n = 0, 0, len(s)
        while r < n:
            while r < n and s[r] != ' ':
                r += 1
            _l, _r = l, r - 1
            while _l < _r:
                s[_l], s[_r] = s[_r], s[_l]
                _l += 1
                _r -= 1
            l = r + 1
            r += 1
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
