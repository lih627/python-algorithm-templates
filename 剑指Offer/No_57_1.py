class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, _ in enumerate(nums):
            if _ not in d:
                d[target - _] = _
            else:
                return [d[_], _]
