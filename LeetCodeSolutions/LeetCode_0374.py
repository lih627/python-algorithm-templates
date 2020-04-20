# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            cmp = guess(mid)
            if cmp == 1:
                l = mid + 1
            elif cmp == -1:
                r = mid - 1
            else:
                return mid
