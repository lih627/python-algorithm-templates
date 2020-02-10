class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(idx, tmp):
            res.append(tmp)
            for idx in range(idx, n):
                helper(idx + 1, tmp + [nums[idx]])

        helper(0, [])
        return res
