# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(node):
            if not node:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return res
