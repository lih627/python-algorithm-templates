from typing import List
import collections


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = [[-v, k] for (k, v) in counter.items()]
        import heapq
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
