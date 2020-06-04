class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for item in zip(startTime, endTime):
            if item[0] <= queryTime <= item[1]:
                cnt += 1
        return cnt
