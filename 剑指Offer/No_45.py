class Solution:
    def minNumber(self, nums: List[int]) -> str:
        import functools
        def compare(x, y):
            if int(x + y) < int(y + x):
                return -1
            if int(x + y) > int(y + x):
                return 1
            return 0

        tmp = [str(_) for _ in nums]
        tmp.sort(key=functools.cmp_to_key(compare))
        return ''.join(tmp)
