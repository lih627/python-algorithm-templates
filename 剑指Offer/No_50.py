class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        from collections import Counter
        counter = Counter(list(s))
        for _ in s:
            if counter[_] == 1:
                return _
        return ' '
