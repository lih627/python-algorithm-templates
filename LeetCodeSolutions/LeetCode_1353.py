from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        visited = set()
        for event in events:
            for i in range(event[0], event[1] + 1):
                if i not in visited:
                    visited.add(i)
                    break
        return len(visited)


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        优先队列
        """
        max_day = 0
        import collections
        import heapq
        start_map = collections.defaultdict(list)
        for event in events:
            start_map[event[0]].append(event[1])
            max_day = max(max_day, event[1])
        cnt = 0
        heap = []
        for i in range(1, max_day + 1):
            while heap and heap[0] < i:
                heapq.heappop(heap)
            if i in start_map:
                while start_map[i]:
                    heapq.heappush(heap, start_map[i].pop())
            if heap:
                cnt += 1
                heapq.heappop(heap)
        return cnt
