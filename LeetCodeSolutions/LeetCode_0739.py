from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Use stack
        """
        ans = [0] * len(T)
        stack = []
        for _ in range(len(T) - 1, -1, -1):
            while stack and T[_] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[_] = stack[-1] - _
            stack.append(_)
        return ans
