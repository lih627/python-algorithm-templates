"""
LeetCode 0705:
design hash set

list + BST
"""


class HashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 853
        self.hashtable = [None] * self.n

    def add(self, key: int) -> None:
        idx = key % self.n
        if not self.hashtable[idx]:
            self.hashtable[idx] = BST(key)
        else:
            tree = self.hashtable[idx]
            if not tree.search(key):
                tree.insert(key)

    def remove(self, key: int) -> None:
        idx = key % self.n
        if not self.hashtable[idx]:
            return None
        else:
            tree = self.hashtable[idx]
            if tree.search(key):
                tree.delete(key)
            if tree.isNone():
                # print(idx, self.hashtable[idx])
                self.hashtable[idx] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.n
        if not self.hashtable[idx]:
            return False
        else:
            tree = self.hashtable[idx]
            # if key in (43, 974, 856, 616):
            #     print('Tree:', tree)
            #     print('cur_key: {}, result: {}'.format(key, tree.search(key)))
            return tree.search(key)


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self, val):
        self.root = TreeNode(val)

    def search(self, val):
        """
        Find val in BST
        return True if any node.val == val
        """

        def helper(node, val):
            if not node:
                return False
            if node.val > val:
                return helper(node.left, val)
            elif node.val < val:
                return helper(node.right, val)
            else:
                return True

        return helper(self.root, val)

    def insert(self, val):
        """
        insert node with val in the BST
        """
        node = self.root
        while node.val != val:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                node = node.right

    def _successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node

    def _predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node

    def delete(self, val):
        """
        delete the node with val in BST
        """

        def helper(node, val):
            if node.val > val:
                node.left = helper(node.left, val)
            elif node.val < val:
                node.right = helper(node.right, val)
            else:
                if not node.left and not node.right:
                    return None
                elif node.right:
                    node.val = self._successor(node).val
                    node.right = helper(node.right, node.val)
                else:
                    node.val = self._predecessor(node).val
                    node.left = helper(node.left, node.val)
            return node

        self.root = helper(self.root, val)

    def isNone(self):
        if self.root is None:
            return True
        return False

    def __repr__(self):
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(str(node.val))
            helper(node.right)

        helper(self.root)
        return ' '.join(res)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
