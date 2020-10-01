# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        tmp = 0

        def helper(node):
            nonlocal tmp
            if node:
                helper(node.right)
                tmp += node.val
                node.val = tmp
                helper(node.left)

        helper(root)
        return root
