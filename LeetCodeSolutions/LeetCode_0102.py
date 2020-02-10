# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        tmp = [root]
        while tmp:
            res.append([_.val for _ in tmp])
            c = []
            for _ in tmp:
                if _.left:
                    c.append(_.left)
                if _.right:
                    c.append(_.right)
            tmp = c
        return res
