class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        fmax, smax = 1, 0
        if nums[fmax] < nums[smax]:
            fmax, smax = smax, fmax
        for idx, _ in enumerate(nums):
            if idx < 2:
                continue
            # print(idx, _, nums[fmax], fmax, smax)
            if _ > nums[fmax]:
                smax = fmax
                fmax = idx
            elif _ > nums[smax]:
                smax = idx

        print(fmax)
        print(smax)
        if nums[fmax] >= 2 * nums[smax]:
            return fmax
        return -1
