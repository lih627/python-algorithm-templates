# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, low=float('-inf'), up=float('inf')):
            if not node: return True
            val = node.val

            if val <= low or val >= up:
                return False
            if not helper(node.left, low, val):
                return False
            if not helper(node.right, val, up):
                return False
            return True

        return helper(root)
