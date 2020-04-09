# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        used_p = False
        stack = [(root, False)]
        while stack:
            node, used = stack.pop()
            if node == p:
                used_p = True
            if not used:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
            else:
                if used_p and node.val > p.val:
                    return node
        return None
