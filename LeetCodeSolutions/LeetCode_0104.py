# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        que = deque()
        que.append((1, root))
        while que:
            cnt, node = que.popleft()
            if node.left:
                que.append((cnt + 1, node.left))
            if node.right:
                que.append((cnt + 1, node.right))
        return cnt
