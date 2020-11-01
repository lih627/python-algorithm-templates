class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        left = [1] * n
        right = [1] * n
        for idx, val in enumerate(A):
            if idx == 0:
                continue
            if val > A[idx - 1]:
                left[idx] += left[idx - 1]

        for idx in range(n - 2, -1, -1):
            if A[idx] > A[idx + 1]:
                right[idx] += right[idx + 1]

        ret = 0
        for l, r in zip(left, right):
            if l > 1 and r > 1:
                ret = max(ret, l + r - 1)
        return ret if ret >= 3 else 0
