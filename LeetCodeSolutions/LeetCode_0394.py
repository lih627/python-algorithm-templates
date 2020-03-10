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

    def decodeString2(self, s):
        stack = []
        for _ in s:
            if _ == ']':
                res = ''
                tmp = stack.pop()
                while tmp != '[':
                    res = tmp + res
                    tmp = stack.pop()
                nums = ''
                while stack and '0' <= stack[-1] <= '9':
                    nums = stack.pop() + nums
                stack.append(int(nums) * res)
            else:
                stack.append(_)
        return ''.join(stack)
