from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        import functools
        @functools.lru_cache(None)
        def helper(s):
            if s in wordDict:
                return True
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    if helper(s[n:]):
                        return True
            return False

        return helper(s)
