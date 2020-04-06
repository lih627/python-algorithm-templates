# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        from collections import deque
        que = deque()
        if not root:
            return 0
        que.append([root, root.val])
        while que:
            n = len(que)
            for i in range(n):
                node, pre = que.popleft()
                isleaf = True
                if node.left:
                    que.append([node.left, node.left.val + pre * 10])
                    isleaf = False
                if node.right:
                    que.append([node.right, node.right.val + pre * 10])
                    isleaf = False
                if isleaf:
                    res += pre
        return res
