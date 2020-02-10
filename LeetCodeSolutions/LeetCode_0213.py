class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def rob_once(tmp):
            if not tmp:
                return 0
            preMax = 0
            curMax = tmp[0]
            i = 1
            while i < len(tmp):
                preMax, curMax = curMax, max(
                    preMax + tmp[i], curMax)
                i += 1
            return max(preMax, curMax)

        return max(nums[0], rob_once(nums[1:]), rob_once(nums[:-1]))
