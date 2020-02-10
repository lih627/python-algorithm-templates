# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from queue import Queue
        if not root:
            return
        que = [root]
        res = []
        while que:
            values = [_.val for _ in que]
            res.append(sum(values) / len(values))
            tmp = []
            for _ in que:
                if _.left:
                    tmp.append(_.left)
                if _.right:
                    tmp.append(_.right)
            que = tmp
        return res
