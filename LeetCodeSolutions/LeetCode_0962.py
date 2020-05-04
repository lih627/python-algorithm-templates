class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        stack = []
        for idx, val in enumerate(A):
            if not stack or stack[-1][0] > val:
                stack.append([val, idx])
        n = len(A)
        for i in range(n - 1, -1, -1):
            if stack and i == stack[-1][1]:
                stack.pop()
            while stack and A[i] >= stack[-1][0]:
                ans = max(ans, i - stack[-1][1])
                stack.pop()
        return ans
