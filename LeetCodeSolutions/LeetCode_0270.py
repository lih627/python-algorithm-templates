# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        pre = float('inf')
        nex = float('inf')
        node = root
        while node:
            if target > node.val:
                if abs(pre - target) > abs(node.val - target):
                    pre = node.val
                node = node.right
            elif target < node.val:
                if abs(nex - target) > abs(node.val - target):
                    nex = node.val
                nex = node.val
                node = node.left
            else:
                return node.val
        print(pre, nex)
        if abs(pre - target) < abs(nex - target):
            return pre
        else:
            return nex
