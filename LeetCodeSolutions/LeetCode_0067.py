class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        la = len(a)
        lb = len(b)
        l = max(la, lb)
        a = a.rjust(l, '0')
        b = b.rjust(l, '0')
        carry = 0
        i = l - 1
        while i > -1:
            tmp, carry = self.stradd(a[i], b[i], carry)
            res = tmp + res
            i -= 1
        if carry:
            res = '1' + res
        return res

    def stradd(self, a, b, carry):
        if (a == '0' and b == '0'):
            if carry:
                return '1', 0
            else:
                return '0', 0
        if (a == '0' and b == '1') or (a == '1' and b == '0'):
            if carry:
                return '0', 1
            else:
                return '1', 0
        if (a == '1' and b == '1'):
            if carry:
                return '1', 1
            else:
                return '0', 1
