# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def helper(node):
            nonlocal res
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            res = max(left + right, res)
            return max(left, right) + 1

        helper(root)
        return res
