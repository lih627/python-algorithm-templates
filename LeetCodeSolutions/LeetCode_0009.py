class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        if n < 0:
            return False
        if n == 0: return True
        if n % 10 == 0:
            return False
        tmp = 10
        org = n
        res = 0
        while n:
            res = res * 10 + n % tmp
            n //= tmp
        print(org, res)
        return org == res
