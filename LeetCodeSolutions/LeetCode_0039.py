from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def backtrack(i, tmp, cur_sum):
            if cur_sum == target:
                res.append(tmp)
                return
            if cur_sum > target or i == n:
                return

            backtrack(i, tmp + [candidates[i]], cur_sum + candidates[i])
            backtrack(i + 1, tmp, cur_sum)

        backtrack(0, [], 0)
        return res
