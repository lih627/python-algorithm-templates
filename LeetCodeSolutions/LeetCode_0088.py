class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:m+n+1] = nums2
        # return nums1.sort()
        idx1, idx2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if idx1 > -1 and idx2 > -1:
                if nums1[idx1] < nums2[idx2]:
                    nums1[i] = nums2[idx2]
                    idx2 -= 1
                else:
                    nums1[i] = nums1[idx1]
                    idx1 -= 1
            elif idx1 == -1 or idx2 == -1:
                nums1[i] = nums1[i] if idx2 == -1 else nums2[i]
