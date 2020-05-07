# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) > target:
            return -1
        lo = 0
        hi = 1
        while tmp := reader.get(hi) <= target:
            lo = hi
            if tmp == target:
                return hi
            hi <<= 1

        while lo <= hi:
            mid = (lo + hi) // 2
            t = reader.get(mid)
            if t == target:
                return mid
            elif t > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
