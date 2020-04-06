# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node):
            if not node:
                return
            if not node.left and not node.right:
                return node
            l = node.left
            r = node.right
            if not r:
                node.left = None
                node.right = l
                return helper(l)
            if not l:
                return helper(r)

            lr = helper(l)
            node.left = None
            node.right = l
            lr.right = r
            return helper(r)

        helper(root)
