from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        prefix = [0] * (n + 1)
        for idx in range(n + 1):
            if idx == 0:
                continue
            prefix[idx] = prefix[idx - 1] + nums[idx - 1]
        cnt = 0
        d = collections.defaultdict(int)
        for idx, val in enumerate(prefix):
            if idx == 0:
                d[0] = 1
                continue
            if val - k in d:
                cnt += d[val - k]
            d[val] += 1
        return cnt
