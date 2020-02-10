class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def helper(idx, tmp):
            if len(tmp) > 1:
                if tuple(tmp) not in visited:
                    res.append(tmp)
                    visited.add(tuple(tmp))

            for i in range(idx, len(nums)):
                if tmp == []:
                    helper(i + 1, [nums[i]])
                else:
                    # print(i, idx, tmp, nums[i])
                    if nums[i] >= tmp[-1]:
                        helper(i + 1, tmp + [nums[i]])

        helper(0, [])
        return res
