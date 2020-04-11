class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:

        def findLarger(n):
            num_digits = num_zeros = num_ones = 0
            find_01 = False
            while n:
                num_digits += 1
                if n & 1:
                    num_ones += 1
                else:
                    num_zeros += 1
                    if num_ones:
                        n >>= 1
                        find_01 = True
                        break
                n >>= 1
            if find_01:
                n <<= 1
                n += 1
                for i in range(num_zeros):
                    n <<= 1
                for i in range(num_ones - 1):
                    n <<= 1
                    n += 1
                return n
            else:
                if num_ones == 1:
                    return 1 << num_digits
                else:
                    res = 2
                    for i in range(num_ones - 1):
                        res <<= 1
                        res += 1
                    return res

        def findSmaller(n):
            num_digits = num_ones = num_zeros = 0
            find_10 = False
            while n:
                num_digits += 1
                if not n & 1:
                    num_zeros += 1
                else:
                    num_ones += 1
                    if num_zeros:
                        find_10 = True
                        n >>= 1
                        break
                n >>= 1
            if find_10:
                n <<= 1
                for i in range(num_ones):
                    n <<= 1
                    n += 1
                for i in range(num_zeros - 1):
                    n <<= 1
                return n
            else:
                return -1

        return [findLarger(num), findSmaller(num)]
