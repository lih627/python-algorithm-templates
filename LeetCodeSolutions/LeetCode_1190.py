class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for _ in s:
            if _ == ')':
                tmp = stack.pop()
                stack2 = []
                while tmp != '(':
                    stack2.append(tmp)
                    tmp = stack.pop()
                stack.extend(stack2)
            else:
                stack.append(_)
        return ''.join(stack)
