class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for idx, val in enumerate(nums):
            while stack and val < stack[-1] and len(stack) + len(nums) - idx - 1 >= k:
                stack.pop()
            stack.append(val)
        return stack[:k]
