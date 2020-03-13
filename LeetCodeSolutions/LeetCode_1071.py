class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = math.gcd(len(str1), len(str2))
        if str1 + str2 == str2 + str1:
            return str1[:n]
        return ''
