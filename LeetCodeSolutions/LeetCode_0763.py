class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        parts = {}
        for idx, c in enumerate(S):
            if c not in parts:
                parts[c] = [idx, idx]
            else:
                parts[c][1] = idx
        _parts = [v for k, v in parts.items()]
        _parts.sort()
        ret = []
        cur = _parts[0]
        for s, e in _parts[1:]:
            if s > cur[1]:
                ret.append(cur[1] - cur[0] + 1)
                cur = [s, e]
            else:
                cur[1] = max(e, cur[1])
        ret.append(cur[1] - cur[0] + 1)
        return ret
