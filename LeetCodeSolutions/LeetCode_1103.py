from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people

        def compute(x):
            return (1 + num_people * x) * num_people * x // 2

        nums = 0
        while compute(nums + 1) < candies:
            nums += 1
        rest = candies - compute(nums)
        for i in range(1, num_people + 1):
            res[i - 1] = (i + i + num_people * (nums - 1)) * nums // 2
        i = 0
        cur = nums * num_people + 1
        while rest > 0:
            if cur > rest:
                cur = rest
            res[i] += cur
            i += 1
            rest -= cur
            cur += 1
        return res
