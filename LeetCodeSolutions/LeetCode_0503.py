class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        res = [-1] * len(nums)
        stack = []
        for idx, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                _, iidx = stack.pop()
                res[iidx] = num
            stack.append([num, idx])
        return res[: len(res) // 2]
