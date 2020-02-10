class Solution:
    def decodeString(self, s: str) -> str:
        strs = s
        res, num, s = '', 0, []
        for _ in strs:
            if _ == '[':
                s.append((res, num))
                res, num = '', 0
            elif _ == ']':
                tmp = s.pop()
                res = tmp[0] + tmp[1] * res
            elif '0' <= _ <= '9':
                num = 10 * num + int(_)
            else:
                res += _
        return res
