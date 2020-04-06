# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        from collections import deque
        que = deque()
        que.append([root, root.val])
        while que:
            node, cur = que.popleft()
            if node.right:
                que.append([node.right, cur + node.right.val])
            if node.left:
                que.append([node.left, cur + node.left.val])
            if not node.right and not node.left:
                if cur == sum:
                    return True
        return False
