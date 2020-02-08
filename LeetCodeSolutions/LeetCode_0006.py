class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        gap = numRows + numRows - 2
        res = ''
        n = len(s)
        for i in range(numRows):
            tmp = i
            if tmp == 0 or tmp == numRows - 1:
                ggap = (gap, gap)
            else:
                ggap = (gap - (tmp * 2), tmp * 2)
            while tmp < n:
                for g in ggap:
                    res += s[tmp]
                    tmp += g
                    if tmp > n - 1:
                        break
        return res
