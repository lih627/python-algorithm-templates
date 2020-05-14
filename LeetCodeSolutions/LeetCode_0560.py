from typing import List
import collections


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


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        for idx, val in enumerate(nums):
            if idx == 0:
                prefix.append(val)
            else:
                prefix.append(val + prefix[-1])
        ans = 0
        import collections
        cnt = collections.defaultdict(int)
        cnt[0] += 1
        for idx, val in enumerate(prefix):
            if val - k in cnt:
                ans += cnt[val - k]
            cnt[val] += 1
        return ans
