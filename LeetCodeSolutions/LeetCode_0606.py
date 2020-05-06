# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        def helper(node):
            if not node:
                return ''
            l = helper(node.left)
            r = helper(node.right)
            if r == '':
                if l != '':
                    return "{}({})".format(node.val, l)
                else:
                    return "{}".format(node.val)
            else:
                return "{}({})({})".format(node.val, l, r)

        return helper(t)
