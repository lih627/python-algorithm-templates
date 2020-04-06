class Solution:
    def numTrees(self, n: int) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(n):
            if n <= 1:
                return 1
            return sum([helper(i) * helper(n - 1 - i) for i in range(n)])

        return helper(n)
