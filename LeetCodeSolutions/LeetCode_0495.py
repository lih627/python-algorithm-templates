class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        n = len(timeSeries)
        for idx, val in enumerate(timeSeries):
            if idx < n - 1 and val + duration > timeSeries[idx + 1]:
                res += timeSeries[idx + 1] - val
            else:
                res += duration
        return res
