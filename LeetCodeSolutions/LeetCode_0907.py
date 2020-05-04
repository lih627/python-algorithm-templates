class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        n = len(A)
        prefix = [None] * n
        for i in range(n):
            while stack and A[i] < A[stack[-1]]:
                stack.pop()
            prefix[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        suffix = [None] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            suffix[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        MOD = 10 ** 9 + 7
        res = 0
        for i in range(n):
            res += prefix[i] * suffix[i] * A[i]
            res %= MOD
        return res
