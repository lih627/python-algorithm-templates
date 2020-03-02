from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        i = 0
        nums.sort()
        res = []
        while i < n - 3:
            if nums[i] > target > 0:
                break
            curr_target = target - nums[i]
            # 2 pointer for 3 sum
            for left in range(i + 1, n - 2):
                middle, right = left + 1, n - 1
                if nums[left] > curr_target > 0:
                    break
                if left > i + 1 and nums[left - 1] == nums[left]:
                    continue
                while middle < right:
                    curr_sum = nums[left] + nums[middle] + nums[right]
                    if curr_sum < curr_target:
                        while middle < right and nums[middle] == nums[middle + 1]:
                            middle += 1
                        middle += 1
                    elif curr_sum > curr_target:
                        while right > middle and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    else:
                        res.append([
                            nums[i], nums[left], nums[middle], nums[right]
                        ])
                        while middle < right and nums[middle] == nums[middle + 1]:
                            middle += 1
                        middle += 1
                        while right > middle and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
            while i < n - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res
