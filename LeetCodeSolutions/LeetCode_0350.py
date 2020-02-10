class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def getmap(nums):
            d = {}
            for _ in nums:
                if _ not in d:
                    d[_] = 1
                else:
                    d[_] += 1
            return d

        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        if n1 < n2:
            m = getmap(nums1)
            for _ in nums2:
                if _ in m and m[_] > 0:
                    res.append(_)
                    m[_] -= 1

        else:
            m = getmap(nums2)
            for _ in nums1:
                if _ in m and m[_] > 0:
                    res.append(_)
                    m[_] -= 1
        return res
