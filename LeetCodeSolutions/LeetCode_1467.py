import math
import itertools


class Solution:
    def getProbability(self, balls: List[int]) -> float:

        def multional(nums):
            return math.factorial(sum(nums)) / math.prod([math.factorial(_) for _ in nums])

        n, cnt = sum(balls) / 2, 0
        t = [range(_ + 1) for _ in balls]
        t = list(itertools.product(*t))
        for i in range(len(t)):
            if sum(t[i]) == n and t[i].count(0) == t[-i - 1].count(0):
                cnt += multional(t[i]) * multional(t[-i - 1])
        return cnt / multional(balls)
