# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pres, ins):
            if not pres or not ins:
                return None
            root = TreeNode(pres[0])
            idx = ins.index(root.val)
            root.left = helper(pres[1: idx + 1], ins[:idx])
            root.right = helper(pres[idx + 1:], ins[idx + 1:])
            return root

        return helper(preorder, inorder)
