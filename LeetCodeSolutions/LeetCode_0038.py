class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = '1'
        cur = 1
        while cur < n:
            l = len(res)
            if l == 1:
                res = '1' + res
            else:
                cnt = 1
                _ = 0
                tmp = ''
                while _ < l:
                    if _ < l - 1 and res[_] == res[_ + 1]:
                        cnt += 1
                    elif _ < l - 1 and res[_] != res[_ + 1]:
                        tmp += str(cnt) + res[_]
                        cnt = 1
                    else:
                        tmp += str(cnt) + res[_]
                    _ += 1
                res = tmp
            cur += 1
        return res
