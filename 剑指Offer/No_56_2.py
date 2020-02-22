class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v == 1:
                return k

    def singleNumber_v2(self, nums: List[int]) -> int:
        # add bit operation solution
        res = 0
        for i in range(32):
            cnt = 0
            bit = 1 << i
            for _ in nums:
                if bit & _:
                    cnt += 1
            if cnt % 3 != 0:
                res |= bit
        return res
