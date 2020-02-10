class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {'+', '-', '*', '/'}
        stack = []
        for _ in tokens:
            if not _ in oper:
                stack.append(int(_))
            else:
                tmp2 = stack.pop()
                tmp1 = stack.pop()
                if _ == '+':
                    stack.append(tmp2 + tmp1)
                elif _ == '-':
                    stack.append(tmp1 - tmp2)
                elif _ == '*':
                    stack.append(tmp1 * tmp2)
                elif _ == '/':
                    stack.append(int(tmp1 / tmp2))
            # print(stack)
        return stack[-1]
