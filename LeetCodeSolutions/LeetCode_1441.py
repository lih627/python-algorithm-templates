class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return []
        n = max(target)
        target = set(target)
        res = []
        for i in range(1, n + 1):
            if i in target:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
        return res
