# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cnt, res = 0, []
        nodes = [root]
        while nodes:
            tmp = [_.val for _ in nodes]
            if cnt & 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            tmp = []
            for _ in nodes:
                if _.left:
                    tmp.append(_.left)
                if _.right:
                    tmp.append(_.right)
            cnt += 1
            nodes = tmp
        return res
