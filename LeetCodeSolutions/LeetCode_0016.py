class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = float('inf')
        for left in range(n - 2):
            middle, right = left + 1, n - 1
            if left > 0 and nums[left - 1] == nums[left]:
                continue
            while middle < right:
                curr_ans = nums[middle] + nums[left] + nums[right]
                curr_res = target - curr_ans
                if abs(res) >= abs(curr_res):
                    res = curr_res
                    ans = curr_ans
                if curr_res == 0:
                    return ans
                if curr_res > 0:
                    middle += 1
                if curr_res < 0:
                    right -= 1
            if nums[left] >= target:
                break
        return ans
