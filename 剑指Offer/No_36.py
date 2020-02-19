"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        tmp = []

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            tmp.append(node)
            inorder(node.right)

        inorder(root)
        n = len(tmp)
        for idx, node in enumerate(tmp):
            node.left = tmp[idx - 1]
            node.right = tmp[(idx + 1) % n]
        return tmp[0]
