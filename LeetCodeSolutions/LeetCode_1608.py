class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(101):
            if sum([num >= x for num in nums]) == x:
                return x
        return -1
