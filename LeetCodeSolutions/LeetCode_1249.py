class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = [''] * len(s)
        for idx, val in enumerate(s):
            if val == '(':
                stack.append([idx, '('])
                res[idx] = '('
            elif val == ')':
                if stack:
                    stack.pop()
                    res[idx] = ')'
            else:
                res[idx] = val
        for tmp in stack:
            res[tmp[0]] = ''
        return ''.join(res)
