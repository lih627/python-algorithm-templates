class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for idx, w in enumerate(words):
            if w == s:
                return idx
        return -1
