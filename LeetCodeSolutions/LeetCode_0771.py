class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashset = set(J)
        res = 0
        for s in S:
            if s in hashset:
                res += 1
        return res
