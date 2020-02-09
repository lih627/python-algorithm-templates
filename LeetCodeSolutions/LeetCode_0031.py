from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Wiki: Permutation
        Generation in lexicographic order
        按照字典顺序生成的下一个排列
        """

        n = len(nums)
        k = 0

        def reverse(arry, i, j):
            while i < j:
                arry[i], arry[j] = arry[j], arry[i]
                i += 1
                j -= 1

        for idx in range(n - 1, 0, -1):
            if nums[idx - 1] < nums[idx]:
                k = idx
                break
        if not k:
            reverse(nums, k, n - 1)
        else:
            i = 0
            for idx in range(n - 1, -1, -1):
                if nums[idx] > nums[k - 1]:
                    i = idx
                    break
            nums[k - 1], nums[i] = nums[i], nums[k - 1]
            reverse(nums, k, n - 1)
