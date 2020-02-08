class Solution:
    def intToRoman(self, num: int) -> str:
        # greedy algorithm
        val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        nums = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        val, nums = val[::-1], nums[::-1]
        res = ''
        while num > 0:
            for idx, _ in enumerate(val):
                if _ <= num:
                    res += nums[idx]
                    num -= _
                    break
        return res
