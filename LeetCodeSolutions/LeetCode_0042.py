from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        if n < 2:
            return res
        for idx in range(1, n - 1):
            cur_height = height[idx]
            left_height = max(height[:idx])
            right_height = max(height[idx + 1:])
            if cur_height < left_height and cur_height < right_height:
                res += min(left_height, right_height) - cur_height
        return res

    def trap2(self, height: List[int]) -> int:
        # dp
        n = len(height)
        res = 0
        if n < 3:
            return res
        max_left = [0] + height[:-1]
        max_right = height[1:] + [0]
        for i in range(2, n):
            max_left[i] = max(max_left[i], max_left[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i], max_right[i + 1])

        for idx in range(n):
            ch = height[idx]
            lh = max_left[idx]
            rh = max_right[idx]
            if ch < lh and ch < rh:
                res += min(rh, lh) - ch
        return res

    def trap(self, height: List[int]) -> int:
        """
        双指针
        """
        n = len(height)
        res = 0
        if n < 3:
            return res
        max_left = height[0]
        max_right = height[n - 1]
        left = 1
        right = n - 2
        res = 0
        while left <= right:
            max_left = max(height[left - 1], max_left)
            max_right = max(height[right + 1], max_right)
            if max_left < max_right:
                if max_left > height[left]:
                    res += max_left - height[left]
                left += 1
            else:
                if max_right > height[right]:
                    res += max_right - height[right]
                right -= 1
        return res
