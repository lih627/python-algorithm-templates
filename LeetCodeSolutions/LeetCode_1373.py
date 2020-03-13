# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        inf = 10 ** 9
        res = 0

        def helper(node):
            nonlocal res
            # isBST, cur_sum, leftmax, rightmin
            if not node:
                return True, 0, -inf, inf
            lbst, l_sum, llmax, lrmin = helper(node.left)
            rbst, r_sum, rrmax, rrmin = helper(node.right)
            if lbst and rbst and llmax < node.val < rrmin:
                cur_sum = l_sum + r_sum + node.val
                res = max(res, cur_sum)
                return (True, cur_sum, node.val, node.val)
            else:
                return False, 0, -inf, inf

        helper(root)
        return res
