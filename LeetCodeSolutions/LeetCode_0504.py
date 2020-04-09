class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        ispos = True
        if num < 0:
            ispos = False
            num = abs(num)
        while num:
            res = str(num - num // 7 * 7) + res
            num //= 7
        if not ispos:
            res = '-' + res
        return res
