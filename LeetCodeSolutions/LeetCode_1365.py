class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maxn = max(nums)
        cnt = [0] * (maxn + 1)
        for val in nums:
            cnt[val] += 1
        pre = 0
        for idx, val in enumerate(cnt):
            cnt[idx] = pre
            pre += val
        return [cnt[i] for i in nums]
