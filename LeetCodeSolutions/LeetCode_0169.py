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

    def majorityElement2(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
