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


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [[root, False]]
        ret = []
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.append([node.right, False])
                stack.append([node, True])
                stack.append([node.left, False])
            else:
                ret.append(node.val)
        return ret
