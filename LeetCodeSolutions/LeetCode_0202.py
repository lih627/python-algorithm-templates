class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num):
            return sum([int(_) ** 2 for _ in str(num)])

        visited = set()
        while True:
            nex = get_next(n)
            if nex in visited:
                return False
            else:
                visited.add(nex)
            if nex == 1:
                return True
            n = nex
