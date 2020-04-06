from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        end = -1
        for interval in intervals:
            if interval[0] < end:
                return False
            end = max(end, interval[1])
        return True
