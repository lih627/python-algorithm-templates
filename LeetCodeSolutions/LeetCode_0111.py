# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        import collections
        que = collections.deque()
        que.append([root, 1])
        while que:
            node, cnt = que.popleft()
            if not node.right and not node.left:
                return cnt
            if node.left:
                que.append([node.left, cnt + 1])
            if node.right:
                que.append([node.right, cnt + 1])
