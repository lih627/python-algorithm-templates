class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return min(numbers)

    def minArray2(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]
