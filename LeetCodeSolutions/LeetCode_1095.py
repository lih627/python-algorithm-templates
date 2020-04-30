# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mval = mountain_arr.get(mid)
            nex = mountain_arr.get(mid + 1)
            pre = mountain_arr.get(mid - 1)
            if pre > mval:
                hi = mid
            elif mval < nex:
                lo = mid + 1
            else:
                break

        if target > mval:
            return -1
        elif target == mval:
            return mid

        def bisearch(lo, hi, target, reverse=False):
            while lo <= hi:
                mid = (lo + hi) // 2
                mval = mountain_arr.get(mid)
                if mval == target:
                    return mid
                elif mval > target:
                    if not reverse:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if not reverse:
                        lo = mid + 1
                    else:
                        hi = mid - 1
            return -1

        left = bisearch(0, mid - 1, target)
        return left if left != -1 else bisearch(mid + 1, n - 1, target, True)
