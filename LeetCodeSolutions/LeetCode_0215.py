from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    def findKthLargest_partition(self, nums: List[int], k: int) -> int:
        """
        partition
        Top-K algorithm
        """

        k = len(nums) - k
        if k < 0:
            return None

        def __partition(low, high):
            random_idx = random.randint(low, high)
            nums[low], nums[random_idx] = nums[random_idx], nums[low]
            x = nums[low]
            i = low
            j = high
            while i < j:
                while i <= j and nums[i] <= x:
                    i += 1
                while j >= i and nums[j] >= x:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[j], nums[low] = nums[low], nums[j]
            return j

        low, high = 0, len(nums) - 1
        while low < high:
            pivot = __partition(low, high)
            if pivot == k:
                break
            elif pivot < k:
                low = pivot + 1
            else:
                high = pivot - 1
        return nums[k]
