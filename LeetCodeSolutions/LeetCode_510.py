# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ret = float('inf')
        pre = -1
        stack = [[root, False]]
        while stack:
            node, visited = stack.pop()
            if not visited:
                if node.right:
                    stack.append([node.right, False])
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
            else:
                if pre == -1:
                    pre = node.val
                else:
                    ret = min(ret, abs(node.val - pre))
                    pre = node.val
        return ret
