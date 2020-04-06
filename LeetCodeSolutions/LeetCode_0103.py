# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        res = []
        if not root:
            return res
        que = deque()
        que.append(root)
        l2r = True
        while que:
            n = len(que)
            tmp = []
            for i in range(n):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if l2r:
                res.append(tmp[:])
                l2r = False
            else:
                res.append(tmp[::-1])
                l2r = True
        return res
