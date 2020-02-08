from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx, num in enumerate(nums):
            if target - num not in res:
                res.update({num: idx})
            else:
                return [res[target - num], idx]
