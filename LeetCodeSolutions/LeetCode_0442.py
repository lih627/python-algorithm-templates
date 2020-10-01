class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = set()
        idx = 0
        while idx < len(nums):
            # print(idx, nums)
            val = nums[idx]
            target_idx = val - 1
            # print(val, target_idx, idx)
            if target_idx == idx:
                idx += 1
            elif nums[target_idx] == val:
                ret.add(val)
                idx += 1
            else:
                nums[idx], nums[target_idx] = nums[target_idx], nums[idx]
        return list(ret)
