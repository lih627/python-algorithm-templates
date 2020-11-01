def _pre(s):
    stack = []
    for c in s:
        if c == '#':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    return stack


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return _pre(S) == _pre(T)
