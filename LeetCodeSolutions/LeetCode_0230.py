# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [[root, False]]
        cnt = 0
        while stack:
            node, visited = stack.pop()
            if not visited:
                if node.right:
                    stack.append([node.right, False])
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
            else:
                cnt += 1
                if cnt == k:
                    return node.val
