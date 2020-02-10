class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
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
