from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        '''
        A [1, 2, 3, 0, 0, 0]
             <-- pa   <-- cur
        B [1, 2, 3]
             <-- pb 
        
        '''
        pa = m - 1
        pb = n - 1
        cur = m + n - 1
        while pa > -1 and pb > -1:
            if A[pa] > B[pb]:
                A[cur] = A[pa]
                pa -= 1
            else:
                A[cur] = B[pb]
                pb -= 1
            cur -= 1
        if pb != -1:
            A[:pb + 1] = B[:pb + 1]
