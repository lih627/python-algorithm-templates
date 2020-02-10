from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        visited = set()
        res = []
        n = len(candidates)
        candidates.sort()

        def helper(idx, cur_sum, tmp):
            if cur_sum == target:
                if tuple(tmp) not in visited:
                    visited.add(tuple(tmp))
                    res.append(tmp)
                return
            if cur_sum > target:
                return
            if idx == n:
                return
            helper(idx + 1, cur_sum + candidates[idx], tmp + [candidates[idx]])
            helper(idx + 1, cur_sum, tmp[:])

        helper(0, 0, [])
        return res
