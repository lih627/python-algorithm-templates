#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class TrieNode:

    def __init__(self):
        self.childs = [None] * 26
        self.isEnd = False


def _trans(c):
    return ord(c) - ord('a')


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            idx = _trans(c)
            if not node.childs[idx]:
                node.childs[idx] = TrieNode()
            node = node.childs[idx]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            idx = _trans(c)
            if not node.childs[idx]:
                return False
            node = node.childs[idx]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            idx = _trans(c)
            if not node.childs[idx]:
                return False
            node = node.childs[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
