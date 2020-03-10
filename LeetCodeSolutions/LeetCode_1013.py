from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sums = sum(A)
        if sums % 3:
            return False
        sums //= 3
        cur_sum, cnt = 0, 0
        for tmp in A:
            cur_sum += tmp
            if cur_sum == sums:
                cnt += 1
                cur_sum = 0
        return cnt >= 3
