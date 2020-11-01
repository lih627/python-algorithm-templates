from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        @lru_cache(None)
        def help(j):
            if j == -1:
                return [[]]
            ret = []
            for k in range(j, -1, -1):
                cur_word = s[k: j + 1]
                if cur_word in wordSet:
                    tmp = help(k - 1)
                    for item in tmp:
                        ret.append(item + [cur_word])
            return ret

        ret = help(len(s))
        return [' '.join(item) for item in ret]
