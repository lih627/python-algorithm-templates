class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmax = [0] * len(nums)
        dpmin = [0] * len(nums)
        for idx, _ in enumerate(nums):
            if idx == 0:
                dpmax[idx] = dpmin[idx] = _
            else:
                if _ >= 0:
                    dpmax[idx] = max(dpmax[idx - 1] * _, _)
                    dpmin[idx] = min(dpmin[idx - 1] * _, _)
                else:
                    dpmax[idx] = max(dpmin[idx - 1] * _, _)
                    dpmin[idx] = min(dpmax[idx - 1] * _, _)
        return max(dpmax)
