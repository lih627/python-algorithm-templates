from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if i[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)
