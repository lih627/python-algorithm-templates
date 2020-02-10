class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = (k + 1) % len(nums)
        tmp = nums[k:] + nums[:k]
        for idx, _ in enumerate(tmp):
            nums[idx] = _
