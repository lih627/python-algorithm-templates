# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = True

        def _helper(node):
            if not node:
                return 0
            left = _helper(node.left) + 1
            right = _helper(node.right) + 1
            if abs(left - right) > 1:
                nonlocal res
                res = False
            return max(left, right)

        _helper(root)
        return res
