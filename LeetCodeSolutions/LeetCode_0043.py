class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        from functools import reduce
        l1, l2 = len(num1) - 1, len(num2) - 1
        # l1 always longer than l2
        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        res = []
        digits = num2[::-1]
        self.digits_visited = {}
        for idx, digit in enumerate(digits):
            if digit not in self.digits_visited:
                tmp = self.StringMulDigit(num1, digit)
                self.digits_visited[digit] = tmp
            res.append(self.digits_visited[digit] + '0' * idx)
        return reduce(self.StringAdd, res)

    def StringMulDigit(self, strs, digit):
        from functools import reduce
        if digit == '0':
            return '0'
        if digit == '1':
            return strs
        strs = strs[::-1]
        res = []
        self.nums_visited = {}
        for idx, elem in enumerate(strs):
            if (elem, digit) not in self.nums_visited:
                tmp = str(int(elem) * int(digit))
                self.nums_visited[(elem, digit)] = tmp
            res.append(self.nums_visited[(elem, digit)] + '0' * idx)
        return reduce(self.StringAdd, res)

    def StringAdd(self, num1, num2):
        l1, l2, carry = len(num1) - 1, len(num2) - 1, 0
        res = ''
        while l1 > -1 or l2 > -1:
            n1 = int(num1[l1]) if l1 > -1 else 0
            n2 = int(num2[l2]) if l2 > -1 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            l1 -= 1
            l2 -= 1
        return '1' + res if carry else res
