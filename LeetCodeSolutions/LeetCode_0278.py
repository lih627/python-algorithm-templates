# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return n
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if not mid or not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid
            else:
                l = mid + 1
