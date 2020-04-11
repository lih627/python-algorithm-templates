# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isSame(node1, node2):
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False
            if not node1 and not node2:
                return True
            if node1.val == node2.val:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
            else:
                return False

        def dfs(node):
            if not node:
                return False
            if node.val == t.val:
                if isSame(node, t):
                    return True
            return dfs(node.left) or dfs(node.right)

        return dfs(s)
