class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import OrderedDict
        if k == 0 or not nums:
            return False
        d = OrderedDict()
        cnt, nums_ = k, nums[:]
        while cnt and nums_:
            tmp = nums_.pop()
            if tmp not in d:
                d[tmp] = 1
            else:
                return True
            cnt -= 1
        while nums_:
            tmp = nums_.pop()
            if tmp not in d:
                d[tmp] = 1
                d.popitem(last=False)
            else:
                return True
        return False
