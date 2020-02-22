from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        O(m + n)
        '''
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

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        O(log(m+n))
        '''
        m = len(nums1)
        n = len(nums2)
        l = m + n
        if l & 1:
            return self.getKth(l // 2, nums1, nums2)
        else:
            left = self.getKth(l // 2 - 1, nums1, nums2)
            right = self.getKth(l // 2, nums1, nums2)
            return (left + right) / 2

    def getKth(self, k, nums1, nums2):
        # k start from 0
        n = len(nums1)
        m = len(nums2)
        # print(k, nums1, nums2)
        if n == 0:
            # print(k, nums2)
            return nums2[k]
        if m == 0:
            return nums1[k]
        # k = 0
        if k == 0:
            return min(nums1[0], nums2[0])
        # k >= 2
        tmp = k // 2 - 1
        tmp = min(tmp, n - 1, m - 1)
        # k = 1
        if tmp == -1:
            tmp = 0
        if nums1[tmp] > nums2[tmp]:
            return self.getKth(k - tmp - 1, nums1, nums2[tmp + 1:])
        else:
            return self.getKth(k - tmp - 1, nums1[tmp + 1:], nums2)
