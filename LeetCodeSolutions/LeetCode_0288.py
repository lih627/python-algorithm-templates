class ValidWordAbbr:

    def trans(self, s):
        if len(s) < 2:
            return s
        else:
            return s[0] + str(len(s) - 2) + s[-1]

    def __init__(self, dictionary: List[str]):
        import collections
        self.hashtable = collections.defaultdict(set)
        for _ in dictionary:
            self.hashtable[self.trans(_)].add(_)

    def isUnique(self, word: str) -> bool:
        s = self.trans(word)
        if word in self.hashtable[s] and len(self.hashtable[s]) == 1:
            return True
        elif len(self.hashtable[s]) == 0:
            return True
        return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
