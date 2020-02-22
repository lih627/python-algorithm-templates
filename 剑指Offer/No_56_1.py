class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        from functools import reduce
        tmp = reduce(lambda x, y: x ^ y, nums)
        cnt = 0
        while tmp & 1 == 0:
            cnt += 1
            tmp >>= 1
        tmp1, tmp2 = 0, 0
        for _ in nums:
            if (_ >> cnt) & 1:
                tmp1 ^= _
            else:
                tmp2 ^= _
        return [tmp1, tmp2]
