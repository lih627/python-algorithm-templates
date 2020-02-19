class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for _ in nums:
            if _ not in d:
                d[_] = 1
                if d[_] > n // 2:
                    return _
            else:
                d[_] += 1
                if d[_] > n // 2:
                    return _
