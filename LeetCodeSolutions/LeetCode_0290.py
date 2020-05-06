class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        pattern = list(pattern)
        str = str.split(' ')
        visited = set()
        if len(pattern) != len(str):
            return False
        for (k, v) in zip(pattern, str):
            if k not in d:
                if v not in visited:
                    visited.add(v)
                else:
                    return False
                d[k] = v
            else:
                if d[k] != v:
                    return False
        return True
