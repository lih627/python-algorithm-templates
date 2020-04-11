from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def isValid(strs):
            stack = []
            for s in strs:
                if s == '(':
                    stack.append(s)
                elif s == ')':
                    if stack:
                        stack.pop()
                    else:
                        return False
            return not stack

        from collections import deque
        que = deque([s])
        visited = set()
        res = []
        findstrs = False
        while que and not findstrs:
            n = len(que)
            for i in range(n):
                word = que.popleft()
                if word not in visited:
                    visited.add(word)
                    if isValid(word):
                        findstrs = True
                        res.append(word)
                    else:
                        for idx, val in enumerate(word):
                            if val in ['(', ')']:
                                que.append(word[:idx] + word[idx + 1:])
        return res
