from heapq import heappop, heappush
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        valid = SortedList(range(k))
        cnt = [0] * k
        heap = []
        for idx, (a, l) in enumerate(zip(arrival, load)):
            c = idx % k
            while heap and heap[0][0] <= a:
                _, v = heappop(heap)
                valid.add(v)
            selected = next(valid.irange(c, k - 1), None)
            if selected is None:
                selected = next(valid.irange(0, k - 1), None)
            if selected is not None:
                cnt[selected] += 1
                valid.remove(selected)
                heappush(heap, [a + l, selected])
        m = max(cnt)
        return [i for i, v in enumerate(cnt) if v == m]
