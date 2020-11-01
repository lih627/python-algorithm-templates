class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        for i in range(2 ** n):
            tmp = []
            idx = 0
            while i:
                if i & 1:
                    tmp.append(nums[idx])
                i >>= 1
                idx += 1
            ret.append(tmp)
        return ret
