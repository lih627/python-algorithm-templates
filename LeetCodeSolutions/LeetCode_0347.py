class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        from heapq import heappush, heappop
        heap = []
        for key in cnt:
            heappush(heap, [-cnt[key], key])
        return [heappop(heap)[1] for i in range(k)]
