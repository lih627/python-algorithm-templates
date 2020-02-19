class Solution:
    def permutation(self, s: str) -> List[str]:
        # import itertools
        # res =  {*map(''.join, itertools.permutations(s))}
        # return res
        elems = list(s)
        elems.sort()
        res = []

        def helper(tmps, s):
            if not tmps:
                res.append(s)
            for idx, _ in enumerate(tmps):
                if idx > 0 and _ == tmps[idx - 1]:
                    continue
                helper(tmps[:idx] + tmps[idx + 1:], s + _)

        helper(elems, '')
        return res
