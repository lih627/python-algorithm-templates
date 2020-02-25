class Solution:
    def strToInt(self, str: str) -> int:
        numeric = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9}
        i = 0
        n = len(str)
        while i < n and str[i] == ' ':
            i += 1
        if i == n:
            return 0

        pos = True
        sign = False
        if str[i] == '+':
            sign = True
        if str[i] == '-':
            sign = True
            pos = False
        if sign:
            i += 1
        if i == n:
            return 0

        if str[i] not in numeric:
            return 0
        res = 0
        while i < n and str[i] in numeric:
            res = 10 * res + numeric[str[i]]
            i += 1
        if pos:
            return min(res, 2 ** 31 - 1)
        if not pos:
            return max(-res, - 2 ** 31)
