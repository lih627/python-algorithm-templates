class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = dict(zip([0, 1, 2, 5, 6, 8, 9], [0, 1, 5, 2, 9, 8, 6]))
        cnt = 0
        for i in range(1, N + 1):
            str_i = str(i)
            tmp = ''
            isvalid = True
            for s in str_i:
                if int(s) in d:
                    tmp += str(d[int(s)])
                else:
                    isvalid = False
                    break
            if isvalid and tmp != str_i:
                cnt += 1
        return cnt
