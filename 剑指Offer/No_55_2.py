# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def balanced(node):
            if not node:
                return True, 0
            lb, l = balanced(node.left)
            rb, r = balanced(node.right)
            if lb and rb and abs(l - r) < 2:
                return True, max(l, r) + 1
            else:
                return False, 0

        return balanced(root)[0]
