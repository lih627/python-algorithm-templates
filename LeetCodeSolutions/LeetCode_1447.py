class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        res = []
        import math
        for a in range(2, n + 1):
            for b in range(1, a):
                if math.gcd(a, b) == 1:
                    res.append(str(b) + '/' + str(a))
        return res
