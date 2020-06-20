# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode):
        ret = float('-inf')

        def helper(node):
            nonlocal ret
            if (not node): return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            ret = max(ret, left + right + node.val)
            return max(right, left) + node.val;

        helper(root)
        return ret
