from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        current_area = (length - 1) * (height[left] if height[left] < height[right] else height[right])
        if length == 2:
            return current_area
        elif height[left] <= height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        return self.compute_area(left, right, height, current_area)

    def compute_area(self, left, right, height, max_area):
        length = right - left
        current_area = length * (height[left] if height[left] < height[right] else height[right])
        if right - left == 1:
            return max(current_area, max_area)
        else:
            if height[left] <= height[right]:
                return self.compute_area(left + 1, right, height, max(max_area, current_area))
            else:
                return self.compute_area(left, right - 1, height, max(max_area, current_area))
