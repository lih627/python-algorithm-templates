class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        elems = {}
        for i in nums:
            if not i in elems:
                elems[i] = 1
            else:
                elems[i] += 1

        tmp = [None for i in nums]
        res = []

        def backtrack(cur_idx=0):
            if cur_idx == len(nums):
                res.append(tmp[:])
                return
            for i in elems:
                if elems[i] > 0:
                    tmp[cur_idx] = i
                    elems[i] -= 1
                    backtrack(cur_idx + 1)
                    elems[i] += 1

        backtrack()
        return res
