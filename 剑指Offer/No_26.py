# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isMatch(a, b):
            if not b:
                return True
            elif not a:
                return False
            elif a.val != b.val:
                return False
            else:
                return isMatch(a.left, b.left) and isMatch(a.right, b.right)

        def helper(a, b):
            res = False
            if not b or not a:
                return False
            if a.val == b.val:
                res = isMatch(a, b)
            if res:
                return True
            else:
                return helper(a.left, b) or helper(a.right, b)

        return helper(A, B)
