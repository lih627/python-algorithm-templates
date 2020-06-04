class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for idx, s in enumerate(sentence):
            if s.startswith(searchWord):
                return idx + 1
        return -1
