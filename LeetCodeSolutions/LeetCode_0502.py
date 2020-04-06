from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        c_p = list(zip(Capital, Profits))
        import heapq
        heapq.heapify(c_p)
        heap = []
        res = W
        for i in range(k):
            while c_p and c_p[0][0] <= res:
                heapq.heappush(heap, -heapq.heappop(c_p)[1])
            if heap:
                res -= heapq.heappop(heap)
        return res
