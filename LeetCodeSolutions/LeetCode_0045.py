from typing import List


class Solution:
    '''
    贪心算法
    '''

    def jump(self, nums: List[int]) -> int:
        last_idx = len(nums) - 1
        if last_idx < 1:
            return 0
        ans = 0
        cur = 0
        while cur + nums[cur] < last_idx:
            step_len = nums[cur]
            tmp = 0
            ans += 1
            for _ in range(1, step_len + 1):
                if cur + _ + nums[cur + _] > tmp:
                    tmp = cur + _ + nums[cur + _]
                    idx = cur + _
            cur = idx
        return ans + 1
