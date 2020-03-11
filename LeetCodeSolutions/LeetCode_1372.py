# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0

        def helper(node):
            nonlocal res
            if not node:
                return -1, -1
            ll, lr = helper(node.left)
            rl, rr = helper(node.right)
            l = lr + 1
            r = rl + 1
            res = max(res, l, r)
            return l, r

        helper(root)
        return res
