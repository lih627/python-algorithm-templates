# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [[root, False]]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append([node, True])
                if node.right:
                    stack.append([node.right, False])
                if node.left:
                    stack.append([node.left, False])
            else:
                res.append(node.val)
        return res
