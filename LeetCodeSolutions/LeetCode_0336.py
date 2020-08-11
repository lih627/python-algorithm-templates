#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.flag = -1
        self.childs = [None] * 26


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, pos):
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if node.childs[idx] is None:
                node.childs[idx] = TrieNode()
            node = node.childs[idx]
        node.flag = pos

    def query(self, word):
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if node.childs[idx] is None:
                return -1
            node = node.childs[idx]
        return node.flag


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieTree()
        for idx, word in enumerate(words):
            trie.insert(word[::-1], idx)

        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        ret = []
        for idx, word in enumerate(words):
            n = len(word)
            for l in range(n + 1):
                if isPalindrome(word[:l]):
                    id2 = trie.query(word[l:])
                    if id2 != -1 and id2 != idx:
                        ret.append([id2, idx])

            for r in range(1, n + 1):
                if isPalindrome(word[-r:]):
                    id2 = trie.query(word[:-r])
                    if id2 != -1 and id2 != idx:
                        ret.append([idx, id2])
        return ret

# @lc code=end
