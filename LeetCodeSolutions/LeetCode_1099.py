class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        n = len(A)
        ans = -1
        for l in range(n - 1):
            r = n - 1
            while l < r:
                tmp = A[l] + A[r]
                if tmp >= K:
                    r -= 1
                else:
                    ans = max(tmp, ans)
                    break
        return ans
