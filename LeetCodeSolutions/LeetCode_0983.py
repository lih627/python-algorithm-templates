class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        from functools import lru_cache
        durations = [1, 7, 30]
        days = set(days)

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            if i in days:
                return min([dp(i + d) + c for d, c in zip(durations, costs)])
            else:
                return dp(i + 1)

        return dp(0)


class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        from functools import lru_cache
        durations = [1, 7, 30]
        N = len(days)

        @lru_cache(None)
        def dp(i):
            if i > N - 1:
                return 0
            j = i
            ans = float('inf')
            for d, c in zip(durations, costs):
                while j < N and days[i] + d > days[j]:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans

        return dp(0
