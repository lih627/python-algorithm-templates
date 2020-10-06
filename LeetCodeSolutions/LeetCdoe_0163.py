def lower_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        l, r = lower_bound(nums, lower), lower_bound(nums, upper)
        # print(l, r)
        if lower == upper:
            if l == len(nums) or (l < len(nums) and nums[l] != lower):
                return [str(lower)]
            else:
                return []
        if lower > upper:
            return []
        if r == 0:
            if len(nums) > 0 and nums[0] == upper:
                upper -= 1
            if lower == upper:
                return [str(lower)]
            return ['{}->{}'.format(lower, upper)]
        if l == len(nums):
            return ['{}->{}'.format(lower, upper)]
        ret = []
        if nums[l] > lower:
            _upnum = nums[l] - 1
            if lower == _upnum:
                ret.append(str(lower))
            else:
                ret.append('{}->{}'.format(lower, _upnum))
        while l + 1 < r:
            _lower = nums[l] + 1
            _upper = nums[l + 1] - 1
            if _lower < _upper:
                ret.append('{}->{}'.format(_lower, _upper))
            elif _lower == _upper:
                ret.append(str(_lower))
            l += 1
        if r < len(nums) and upper == nums[r]:
            upper -= 1
        _lower = nums[l] + 1
        _upper = upper
        if _lower < _upper:
            ret.append('{}->{}'.format(_lower, _upper))
        elif _lower == _upper:
            ret.append(str(_lower))
        return ret
