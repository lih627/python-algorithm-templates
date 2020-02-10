class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        for i in [2, 3, 5]:
            while not num % i:
                num /= i
        return num == 1
