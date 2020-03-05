class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        slow, fast = 1, 2
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[slow - 1]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
