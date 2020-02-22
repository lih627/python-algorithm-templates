# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            k -= 1
            node = stack.pop()
            if k == 0:
                return node.val
            node = node.left
