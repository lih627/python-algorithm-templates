# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ret = 0

        def helper(node):
            nonlocal ret
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            ret += abs(l - r);
            return l + r + node.val

        helper(root)
        return ret
