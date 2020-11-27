import collections


class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        ret = ''
        state = collections.defaultdict(bool)
        words.sort(key=lambda x: len(x))
        for w in words:
            if len(w) == 1:
                state[w] = True
                if not ret:
                    ret = w
                else:
                    ret = w if w < ret else ret
            if w[:-1] in s and state[w[:-1]] == True:
                state[w] = True
                if len(w) > len(ret):
                    ret = w
                elif len(w) == len(ret):
                    ret = w if w < ret else ret
        return ret
