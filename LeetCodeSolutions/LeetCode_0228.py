class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r, n = 0, 0, len(nums)
        ret = []
        while r < n:
            while r + 1 < n and nums[r] + 1 == nums[r + 1]:
                r += 1
            if nums[r] == nums[l]:
                ret.append(str(nums[r]))
            else:
                ret.append("{}->{}".format(nums[l], nums[r]))
            r += 1
            l = r
        return ret
