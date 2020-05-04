class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for s in S:
            if s == '(':
                stack.append(0)
            else:
                tmp = max(2 * stack.pop(), 1)
                stack[-1] += tmp
        return stack[0]
