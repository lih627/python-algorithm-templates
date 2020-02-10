class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # print(round(math.log(n, 3)))
        return n > 0 and 3 ** round(math.log(n, 3)) == n
