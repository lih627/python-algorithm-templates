from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(low, high):
            randidx = random.randint(low, high)
            nums[low], nums[randidx] = nums[randidx], nums[low]
            x = nums[low]
            l = low + 1
            r = high
            while l <= r:
                while l <= r and nums[l] <= x:
                    l += 1
                while l <= r and nums[r] >= x:
                    r -= 1
                if l > r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
            nums[r], nums[low] = nums[low], nums[r]
            return r

        def quicksort(low, high):
            if low < high:
                pivot = partition(low, high)
                quicksort(low, pivot - 1)
                quicksort(pivot + 1, high)

        quicksort(0, len(nums) - 1)
        return nums
