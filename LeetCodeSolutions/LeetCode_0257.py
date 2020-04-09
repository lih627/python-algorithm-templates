# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [str(root.val)]

        def helper(node, path):
            if not node.left and not node.right:
                res.append(path)
                return
            if node.left:
                helper(node.left, path + '->' + str(node.left.val))
            if node.right:
                helper(node.right, path + '->' + str(node.right.val))

        helper(root, str(root.val))
        return res
