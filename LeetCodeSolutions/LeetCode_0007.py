class Solution:
    def reverse(self, x: int) -> int:
        pos = x >= 0
        x = abs(x)
        s = list(str(x))
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        # print(s)
        res = int(''.join(s))
        if not pos:
            res = -res
        return res if -0x80000000 <= res <= 0x7FFFFFFF else 0
