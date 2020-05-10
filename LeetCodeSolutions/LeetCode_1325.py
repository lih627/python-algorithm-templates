# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def helper(node):
            if not node:
                return None
            node.right = helper(node.right)
            node.left = helper(node.left)
            if node.val == target:
                if not node.right and not node.left:
                    return None
            return node

        return helper(root)
