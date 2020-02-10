class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        n = len(nums)

        def dfs(idx, cur):
            if idx != n and (idx, cur) not in d:
                d[(idx, cur)] = dfs(idx + 1, cur + nums[idx]) + dfs(idx + 1, cur - nums[idx])
            # print(idx, cur, d.get((idx, cur)))
            return d.get((idx, cur), int(cur == S))

        return dfs(0, 0)
