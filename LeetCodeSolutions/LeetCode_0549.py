# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        ret = 0

        def helper(node):
            nonlocal ret
            if not node:
                return 0, 0
            ld, lu = helper(node.left)
            rd, ru = helper(node.right)
            curd, curu = 1, 1
            if node.left:
                if node.val - node.left.val == 1:
                    curu = lu + 1
                elif node.val - node.left.val == -1:
                    curd = ld + 1
            if node.right:
                if node.val - node.right.val == 1:
                    curu = max(curu, ru + 1)
                elif node.val - node.right.val == -1:
                    curd = max(curd, rd + 1)
            if curu > 1 and curd > 1:
                ret = max(curu + curd - 1, ret)
            else:
                ret = max(ret, curu, curd)
            return curd, curu

        helper(root)
        return ret
