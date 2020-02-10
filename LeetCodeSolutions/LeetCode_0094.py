# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def _inorder(root):
            if not root:
                return
            _inorder(root.left)
            res.append(root.val)
            _inorder(root.right)

        _inorder(root)
        return res
