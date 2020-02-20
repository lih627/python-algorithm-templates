from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = (m + n) // 2
        left = right = float('-inf')
        m_start = n_start = 0
        while i > -1:
            left = right
            if n_start >= n or m_start < m and nums1[m_start] < nums2[n_start]:
                right = nums1[m_start]
                m_start += 1
            else:
                right = nums2[n_start]
                n_start += 1
            i -= 1
        if (m + n) & 1:
            return right
        return (left + right) / 2
