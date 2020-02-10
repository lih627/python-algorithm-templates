class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or '00' in s:
            return 0
        for idx, _ in enumerate(s):
            if idx == 0:
                pre, cur = 1, 1
            else:
                tmp = cur
                if _ != '0':
                    if s[idx - 1] == '0':
                        cur = tmp
                        pre = tmp
                    elif 0 < int(s[idx - 1] + _) < 27:
                        cur = pre + tmp
                        pre = tmp
                    else:
                        cur = tmp
                        pre = tmp
                else:
                    if s[idx - 1] > '2':
                        return 0
                    else:
                        cur = pre
                        pre = tmp
        return cur
