class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for _ in nums:
            if _ not in s:
                s.add(_)
            else:
                return _
