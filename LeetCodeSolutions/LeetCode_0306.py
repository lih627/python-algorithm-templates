class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValid(str1, str2, num):
            if not num:
                return True
            res = str(int(str1) + int(str2))
            # print(str1, str2, res, num)
            str1, str2 = str2, res
            l = len(res)
            return num.startswith(res) and isValid(str1, str2, num[l:])

        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i > 1: return False
            sub1 = num[:i]
            for j in range(1, n):
                if max(i, j) > n - i - j: break
                if num[i] == '0' and j > 1: break
                sub2 = num[i:i + j]
                if isValid(sub1, sub2, num[i + j:]):
                    return True
        return False
