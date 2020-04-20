class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        d1 = {k: v for k, v in zip(list1, range(len(list1)))}
        d2 = {k: v for k, v in zip(list2, range(len(list2)))}
        rests = set(list1) & set(list2)
        minval = float('inf')
        for rest in rests:
            cur = d1[rest] + d2[rest]
            if cur < minval:
                res = []
                minval = cur
                res.append(rest)
            elif cur == minval:
                res.append(rest)
        return res
