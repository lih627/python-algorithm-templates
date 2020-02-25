class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if len(a) < 2:
            return []
        prefix = a[:]
        suffix = a[::-1]
        for elem in (prefix, suffix):
            for idx, _ in enumerate(elem):
                if idx == 0:
                    pass
                else:
                    elem[idx] = _ * elem[idx - 1]
        suffix = suffix[::-1]
        res = [1] * len(a)
        for idx in range(len(res)):
            if idx == 0:
                res[idx] = suffix[1]
            elif idx == len(res) - 1:
                res[idx] = prefix[idx - 1]
            else:
                res[idx] = prefix[idx - 1] * suffix[idx + 1]
        return res
