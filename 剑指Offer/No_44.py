import itertools


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        for digits in itertools.count(1):
            first_num = 10 ** (digits - 1)
            if n <= 9 * first_num * digits:
                n -= 1
                return int(str(first_num + n // digits)[n % digits])
            n -= 9 * first_num * digits
