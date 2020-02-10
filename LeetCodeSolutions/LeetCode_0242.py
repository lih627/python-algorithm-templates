class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if not s and not t:
        #     return True
        # if len(s) != len(t):
        #     return False
        # from functools import reduce
        # tmp = s + t
        # # print(list(tmp))
        # res = reduce(lambda x, y: x ^ y, map(ord, list(tmp)))
        # return not res
        return abs(sum([ord(x) ** 0.5 for x in s]) - sum([ord(y) ** 0.5 for y in t])) < 1e-5
