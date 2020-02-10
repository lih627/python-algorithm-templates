class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        for _ in strs:
            res[tuple(sorted(_))].append(_)
        return res.values()
