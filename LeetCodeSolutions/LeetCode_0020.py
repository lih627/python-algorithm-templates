class Solution:
    def isValid(self, s: str) -> bool:
        pat = {
            '(': 1, ')': -1,
            '{': 2, '}': -2,
            '[': 3, ']': -3
        }
        stack = []
        for _ in s:
            tmp = pat[_]
            if tmp > 0:
                stack.append(tmp)
            else:
                if not stack:
                    return False
                elif stack[-1] + tmp != 0:
                    return False
                stack.pop()
        return not stack
