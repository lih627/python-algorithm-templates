class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        n = len(deck)
        if n < 2:
            return False
        from collections import Counter
        counter = Counter(deck)
        nums = list(counter.values())
        import math
        for idx, val in enumerate(nums):
            if idx == 0:
                cur = val
            else:
                cur = math.gcd(cur, val)
                if cur < 2:
                    return False
        return True
