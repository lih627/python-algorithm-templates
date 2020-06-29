class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)];
        ret = 0;
        for val in nums:
            ret ^= val
        return ret
