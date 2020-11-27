class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        mid, m = -1, -1
        for idx, val in enumerate(A):
            if val > m:
                m = val
                mid = idx
        if mid == 0 or mid == len(A) - 1:
            return False
        for k in range(mid + 1, len(A)):
            if A[k] >= A[k - 1]:
                return False
        for k in range(0, mid):
            if A[k] >= A[k + 1]:
                return False
        return True
