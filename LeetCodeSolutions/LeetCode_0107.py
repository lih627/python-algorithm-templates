# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        import collections
        que = collections.deque()
        res = collections.deque()
        que.append(root)
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
            res.appendleft(tmp[:])
        return list(res)
